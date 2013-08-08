from PyQt4 import QtGui

class Table(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Table, self).__init__(parent)
        layout = QtGui.QGridLayout() 
        self.led = QtGui.QLineEdit("Foobar")
        self.table = QtGui.QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        layout.addWidget(self.led, 0, 0)
        layout.addWidget(self.table, 1, 0)
        self.table.setItem(1, 0, QtGui.QTableWidgetItem(self.led.text()))
        self.setLayout(layout)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    t = Table()
    t.show()
    sys.exit(app.exec_())