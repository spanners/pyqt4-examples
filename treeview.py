# -*- coding: utf-8 -*-
#!/usr/bin/env python


import sys
import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TreeModelTester(QMainWindow):
    """Test correctness of tree models/views """


    def __init__(self):
        """Initialize the application."""

        QMainWindow.__init__(self)

        self.counter = 0

        # Make the GUI
        self.setWindowTitle('TreeView tester')
        self.setupMenus()

        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        self.dbs_tree_view = QTreeView(central_widget)
        central_layout.addWidget(self.dbs_tree_view)

        # The tree of databases model/view
        self.dbs_tree_model = DBsTreeModel(self)
        self.dbs_tree_view.setModel(self.dbs_tree_model)


    def setupMenus(self):
        """Set up the main window menus."""

        remove_action = QAction('&Remove', self)
        remove_action.setShortcut(QKeySequence.Delete)
        self.connect(remove_action, SIGNAL("triggered()"), self.slotRemoveBranch)
        menu = self.menuBar().addMenu('&Menu')
        menu.addAction(remove_action)


    def closeEvent(self, event):
        """Handle close events."""
        qApp.quit()


    def slotRemoveBranch(self):
        """Delete a given branch from the tree model and its views."""

        current = self.dbs_tree_view.currentIndex()
        if current is None:
            return

        # Delete the node
        self.dbs_tree_model.deleteNode(current)


class GroupNode(object):
    """A group node in the tree of databases model."""

    def __init__(self, parent, name):
        """Create a group node for the tree of databases model."""

        self.children = []
        self.parent = parent
        self.name = name


    def __len__(self):
        return len(self.children)


    def insertChild(self, child, position=0):
        """Insert a child in a group node."""
        self.children.insert(position, child)


    def childAtRow(self, row):
        """The row-th child of this node."""

        assert 0 <= row <= len(self.children)
        return self.children[row]


    def row(self):
        """The position of this node in the parent's list of children."""

        if self.parent:
            return self.parent.children.index(self)

        return 0
		
class DBsTreeModel(QAbstractItemModel):
    """The tree of databases model."""

    def __init__(self, parent=None):
        """Create the model."""

        QAbstractItemModel.__init__(self, parent)

        # Populate the model
        self.root = GroupNode(None, 'root')
        for root, dirs, files in os.walk("."):
		    for d in dirs:
			    self.addBranch(QModelIndex(), d)
            #for f in files:
            #    self.addBranch(QModelIndex(), f)

    def flags(self, index):
        """Returns the item flags for the given index. """
        return Qt.ItemIsEnabled|Qt.ItemIsSelectable


    def data(self, index, role):
        """Returns the data stored under the given role for the item
        referred to by the index."""

        if not index.isValid():
            return QVariant()
        node = self.nodeFromIndex(index)
        if role == Qt.DisplayRole:
            return QVariant(node.name)
        else:
            return QVariant()


    def setData(self, index, value, role=Qt.DisplayRole):
        """Sets the role data for the item at index to value."""

        if not index.isValid():
            return False
        node = self.nodeFromIndex(index)
        if role == Qt.DisplayRole:
            node.name = value
            self.emit(SIGNAL(
                'dataChanged(QModelIndex, QModelIndex)'), index, index)
            return True
        return False


    def headerData(self, section, orientation, role):
        """Returns the data for the given role and section in the header
        with the specified orientation.
        """

        if (orientation, role) == (Qt.Horizontal, \
            Qt.DisplayRole):
            return QVariant('Sample tree')

        return QVariant()


    def columnCount(self, parent):
        """The number of columns for the children of the given index."""
        return 1


    def rowCount(self, parent):
        """The number of rows of the given index."""

        if not parent.isValid():
            parent_node = self.root
        else:
            parent_node = parent.internalPointer()
        return len(parent_node)


    def hasChildren(self, index):
        """Finds out if a node has children."""

        if not index.isValid():  # self.root fulfils this condition
            return True
        parent = self.nodeFromIndex(index)
        if parent.children != []:
            return True
        else:
            return False


    def index(self, row, column, parent):
        """Creates an index in the model for a given node and returns it."""

        assert self.root
        branch = self.nodeFromIndex(parent)
        assert branch is not None
        return self.createIndex(row, column, branch.childAtRow(row))


    def nodeFromIndex(self, index):
        """Retrieves the tree node with a given index."""

        if index.isValid():
            return index.internalPointer()
        else:
            return self.root


    def parent(self, child):
        """The parent index of a given index."""

        node = self.nodeFromIndex(child)
        if node is None:
            return QModelIndex()
        parent = node.parent
        if parent is None:
            return QModelIndex()
        grandparent = parent.parent
        if grandparent is None:
            return QModelIndex()
        row = grandparent.rowOfChild(parent)
        assert row != -1
        return self.createIndex(row, 0, parent)


    def deleteNode(self, index):
        """Delete a node from the model."""

        node = self.nodeFromIndex(index)
        # Deletes the node from the tree of databases model/view
        parent = self.parent(index)
        position = node.row()
        self.removeRows(position, 1, parent)


    def addBranch(self, index, childname):
        """Create a new branch under the given parent."""

        self.insertRows(0, 1, index)
        child_idx = self.index(0, 0, index)
        self.setData(child_idx, childname)
        return True


    def insertRows(self, position=0, count=1, parent=QModelIndex()):
        """Insert `count` rows after the given row."""

        node = self.nodeFromIndex(parent)
        self.beginInsertRows(parent, position,
            position + count - 1)
        child = GroupNode(node, 'Unknown')
        node.insertChild(child, position)
        self.endInsertRows()
        return True


    def removeRows(self, position, count=1, parent=QModelIndex()):
        """Removes `count` rows before the given row."""

        node = self.nodeFromIndex(parent)
        self.beginRemoveRows(parent, position,
            position + count - 1)
        for row in range(count):
            del node.children[position + row]
        self.endRemoveRows()
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tester = TreeModelTester()
    tester.show()
    app.exec_()