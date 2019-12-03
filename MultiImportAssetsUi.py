# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiImports.ui'
#
# Created: Mon Nov  4 17:42:48 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import sys,os
import getpass
import threading
#sys.path.append("F:\\svn\\art\\Houdini\\HoudiniTool\\HexTool\\scripts\\python\\UEGui\\python\\Lib\\site-packages")

import ueAssets as uelib
reload(uelib)
USER = getpass.getuser()
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtGui.QMainWindow()

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(427, 142)


        self.pushButton = QtGui.QPushButton(self.MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(270, 80, 100, 20))
        self.pushButton.setObjectName("pushButton")

        self.callSheetLable = QtGui.QLabel(self.MainWindow)
        self.callSheetLable.setGeometry(QtCore.QRect(30, 10, 160, 30))
        self.callSheetLable.setObjectName("callSheetLable")

        self.callsheetpath = QtGui.QLineEdit(self.MainWindow)
        self.callsheetpath.setGeometry(QtCore.QRect(30, 40, 240, 30))
        self.callsheetpath.setObjectName("callsheetpath")

        self.fileBrowser = QtGui.QPushButton(self.MainWindow)
        self.fileBrowser.setGeometry(QtCore.QRect(270, 40, 30, 30))
        self.fileBrowser.setObjectName("fileBrowser")



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


        self.pushButton.clicked.connect(self.ImportAssets)
        self.fileBrowser.clicked.connect(self.openFiles)

    def ImportAssets(self):

        if os.path.exists(self.callsheetpath.text()):
            
            my_lib = uelib.hex_assets()
            my_lib.setCallsheetPath(self.callsheetpath.text())
            my_lib.exportJson()
            my_lib.importMyAssets()
        else:
            print "File Not Exists"
    def openFiles(self):

        filename, filter = QtGui.QFileDialog.getOpenFileName(parent = self.MainWindow,caption='Open file', dir='.', filter='Call Sheet Files (*.json)')
        self.callsheetpath.setText( filename )

        print filename
        

    def printMessage(self):
        print self.callsheetpath.text()

    def retranslateUi(self):
        path = "C:\\Users\\{USER}\\Documents\\tst.json".format(USER = USER)
        self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ImportAssets", None, QtGui.QApplication.UnicodeUTF8))
        self.callSheetLable.setText(QtGui.QApplication.translate("MainWindow", "CallSheet Input Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fileBrowser.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.callsheetpath.setText(QtGui.QApplication.translate("MainWindow", path, None, QtGui.QApplication.UnicodeUTF8))




