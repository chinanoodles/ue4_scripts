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

import splashImport as si
reload(si)
USER = getpass.getuser()
from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtGui.QMainWindow()

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(427, 142)


        self.pushButton = QtGui.QPushButton(self.MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(270, 100, 100, 20))
        self.pushButton.setObjectName("pushButton")

        self.callSheetLable = QtGui.QLabel(self.MainWindow)
        self.callSheetLable.setGeometry(QtCore.QRect(30, 10, 160, 30))
        self.callSheetLable.setObjectName("callSheetLable")

        self.callsheetpath = QtGui.QLineEdit(self.MainWindow)
        self.callsheetpath.setGeometry(QtCore.QRect(30, 40, 240, 30))
        self.callsheetpath.setObjectName("callsheetpath")

        self.asset_path_Lable = QtGui.QLabel(self.MainWindow)
        self.asset_path_Lable.setGeometry(QtCore.QRect(30, 70, 160, 30))
        self.asset_path_Lable.setObjectName("asset_path_Lable")

        self.asset_path = QtGui.QLineEdit(self.MainWindow)
        self.asset_path.setGeometry(QtCore.QRect(30, 100, 240, 30))
        self.asset_path.setObjectName("asset_path")



        self.fileBrowser = QtGui.QPushButton(self.MainWindow)
        self.fileBrowser.setGeometry(QtCore.QRect(270, 40, 30, 30))
        self.fileBrowser.setObjectName("fileBrowser")



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.createSplash)
        self.fileBrowser.clicked.connect(self.openFiles)

    def createSplash(self):
        if os.path.exists(self.callsheetpath.text()):
            my_lib = si.createSplash(self.callsheetpath.text())
        else:
            print ("File Dose Not Exists")
    def openFiles(self):

        filename, filter = QtGui.QFileDialog.getOpenFileName(parent = self.MainWindow,caption='Open file', dir='.', filter='Call Sheet Files (*.json)')
        self.callsheetpath.setText( filename )

        print (filename)
        

    def printMessage(self):
        print (self.callsheetpath.text())

    def retranslateUi(self):
        path = "C:\\Users\\{USER}\\Documents\\tst.json".format(USER = USER)
        content_path = "/Game/OpenWorldAutoImport/"
        self.MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ImportSplash", None, QtGui.QApplication.UnicodeUTF8))
        self.callSheetLable.setText(QtGui.QApplication.translate("MainWindow", "Splash Json Path", None, QtGui.QApplication.UnicodeUTF8))
        self.callsheetpath.setText(QtGui.QApplication.translate("MainWindow", path, None, QtGui.QApplication.UnicodeUTF8))
        self.fileBrowser.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_path_Lable.setText(QtGui.QApplication.translate("MainWindow", "Import UE Path", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_path.setText(QtGui.QApplication.translate("MainWindow", content_path, None, QtGui.QApplication.UnicodeUTF8))


        




