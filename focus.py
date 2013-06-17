from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.label = QLabel('Window')
        self.setCentralWidget(self.label)
        self.setFocusPolicy(Qt.StrongFocus)

    def focusInEvent(self, event):
        self.label.setText('Got focus')

    def focusOutEvent(self, event):
        self.label.setText('Lost focus')

def changedFocusSlot(old, now):
    if (now==None and QApplication.activeWindow()!=None):
        print "set focus to the active window"
        QApplication.activeWindow().setFocus()

def main():
    app = QApplication(sys.argv)
    QObject.connect(app, SIGNAL("focusChanged(QWidget *, QWidget *)"), changedFocusSlot)

    win1 = MyWindow()
    win2 = MyWindow()
    win1.show()
    win2.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()