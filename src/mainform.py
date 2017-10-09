# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created: Tue Sep 26 15:56:44 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pickFileButt = QtGui.QPushButton(self.centralwidget)
        self.pickFileButt.setGeometry(QtCore.QRect(10, 70, 80, 23))
        self.pickFileButt.setObjectName(_fromUtf8("pickFileButt"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 421, 23))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 190, 111, 21))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pickFileButt_2 = QtGui.QPushButton(self.centralwidget)
        self.pickFileButt_2.setGeometry(QtCore.QRect(10, 160, 80, 23))
        self.pickFileButt_2.setObjectName(_fromUtf8("pickFileButt_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 130, 421, 23))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 220, 781, 131))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 150, 80, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pickFileButt.setText(_translate("MainWindow", "Browse..", None))
        self.label.setText(_translate("MainWindow", "Input file:", None))
        self.checkBox.setText(_translate("MainWindow", "Output here:", None))
        self.label_2.setText(_translate("MainWindow", "Output file:", None))
        self.pickFileButt_2.setText(_translate("MainWindow", "Browse..", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))

