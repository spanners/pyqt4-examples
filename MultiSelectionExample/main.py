import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
from MultiSelectionExample import Ui_MSMainWindow


class MSExampleWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.msUi = Ui_MSMainWindow()
        self.msUi.setupUi(self)

        self.connect(self.msUi.msClickHere, QtCore.SIGNAL('clicked()'), self.onClickHere)

    def onClickHere(self):
        selectedItems = self.msUi.msComboBox.checkedItems()
        for item in selectedItems:
            print item

        print ("=" * 25)


if __name__ == "__main__":
    msApp = QtGui.QApplication(sys.argv)
    msApp.setStyle('windowsvista')
    msWindow = MSExampleWindow()
    msWindow.show()
    sys.exit(msApp.exec_())