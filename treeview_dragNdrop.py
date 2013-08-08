# ./treeview_dragNdrop.py
import sys
import os
from PyQt4 import QtGui, QtCore

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.model = QtGui.QStandardItemModel()
        """
        parentItem = self.model.invisibleRootItem()
        k = 0
        for root, dirs, files in os.walk("."):
		    item = QtGui.QStandardItem(QTCore.QString(root).arg(k).arg(i)
            k += 1
        """
        
        for k in range(0, 4):
            parentItem = self.model.invisibleRootItem()
            for i in range(0, 4):
                item = QtGui.QStandardItem(QtCore.QString("item %0 %1").arg(k).arg(i))
                parentItem.appendRow(item)
                parentItem = item

        self.view = QtGui.QTreeView()
        self.view.setModel(self.model)
        self.view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)

        self.setCentralWidget(self.view)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()