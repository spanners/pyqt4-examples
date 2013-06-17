from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
QtGui.qApp = app

pointListBox = QtGui.QTreeWidget()

header=QtGui.QTreeWidgetItem(["Tree","First","secondo"])
#...
pointListBox.setHeaderItem(header)   #Another alternative is setHeaderLabels(["Tree","First",...])

root = QtGui.QTreeWidgetItem(pointListBox, ["root"])
A = QtGui.QTreeWidgetItem(root, ["A"])
barA = QtGui.QTreeWidgetItem(A, ["bar", "i", "ii"])
bazA = QtGui.QTreeWidgetItem(A, ["baz", "a", "b"])


pointListBox.show()
sys.exit(app.exec_())