#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
# In this example, we will use an object from the QtCore module.
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        qbtn = QtGui.QPushButton('Quit', self)
  
        """
        The event processing system in PyQt4 is built with the signal & slot 
        mechanism.

        If we click on the button, the signal `clicked` is emitted.
        The slot can be a Qt slot or any Python callable.
      
        The `QtCore.QCoreApplication` contains the main event loop.
        It processes and dispatches all events.
      
        The `instance()` method gives us it's current instance.
        """
      
        # **NB:** `QtCore.QCoreApplication` is created with the `QtGui.QApplication`
      
        """
        The clicked signal is connected to the `quit()` method, which 
        terminates the application. The communication is done between two 
        objects. The sender and the receiver. The sender is the push button, 
        the receiver is the application object.
        """
        # PyQt4.5 introduced a new style API for working with signals and slots.
        QtCore.QObject.connect(qbtn, QtCore.SIGNAL('clicked()'), QtCore.QCoreApplication.instance().quit)

        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()