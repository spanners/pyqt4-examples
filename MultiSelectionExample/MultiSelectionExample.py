# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiSelectionExample.ui'
#
# Created: Mon Sep 10 00:16:43 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MSMainWindow(object):
    def setupUi(self, MSMainWindow):
        MSMainWindow.setObjectName(_fromUtf8("MSMainWindow"))
        MSMainWindow.resize(442, 79)
        self.centralwidget = QtGui.QWidget(MSMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.msComboBox = MultiCheckComboBox(self.centralwidget)
        self.msComboBox.setObjectName(_fromUtf8("msComboBox"))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.msComboBox.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.msComboBox)
        self.msClickHere = QtGui.QPushButton(self.centralwidget)
        self.msClickHere.setObjectName(_fromUtf8("msClickHere"))
        self.verticalLayout.addWidget(self.msClickHere)
        MSMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MSMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MSMainWindow)

    def retranslateUi(self, MSMainWindow):
        MSMainWindow.setWindowTitle(QtGui.QApplication.translate("MSMainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(0, QtGui.QApplication.translate("MSMainWindow", "India", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(1, QtGui.QApplication.translate("MSMainWindow", "Pakistan", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(2, QtGui.QApplication.translate("MSMainWindow", "Australia", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(3, QtGui.QApplication.translate("MSMainWindow", "South Africaa", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(4, QtGui.QApplication.translate("MSMainWindow", "West Indies", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(5, QtGui.QApplication.translate("MSMainWindow", "England", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(6, QtGui.QApplication.translate("MSMainWindow", "Sri Lanka", None, QtGui.QApplication.UnicodeUTF8))
        self.msComboBox.setItemText(7, QtGui.QApplication.translate("MSMainWindow", "Bangladesh", None, QtGui.QApplication.UnicodeUTF8))
        self.msClickHere.setText(QtGui.QApplication.translate("MSMainWindow", "Selected Items", None, QtGui.QApplication.UnicodeUTF8))

from MultiCheckComboBox import MultiCheckComboBox
