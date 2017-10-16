#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys



# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic



app = QApplication(sys.argv)
#(Ui_MainWindow, QMainWindow) = uic.loadUiType('mainform.ui')
#window = uic.loadUi("MainForm.ui")
MainWindow = uic.loadUi('mainform.ui')
#MainWindow.textEdit.setPlainText('s dfh akjsdhfkajs dhfka sdkjfh aslkjdf hajsdhfkjas asjdkf askd fhak')



class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
      #  self.ui = Ui_MainWindow()
       # self.ui.setupUi(self)


    def db(self):
        print("qweqweqw")

    def ChooseFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        file = open(filename)
        data = file.read()
        self.ui.textEdit_Main.setText(data)

    def helloworld(self):
        self.ui.textEdit.setText("Hello world")
        print ("Hello world again")
        QFileDialog.open(self);

    def __del__(self):
        self.ui = None




#-----------------------------------------------------#
MainWindow.show()
sys.exit(app.exec_())
