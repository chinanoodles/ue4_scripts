# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiImports.ui'
#
# Created: Mon Nov  4 17:42:48 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import sys,os

#sys.path.append("F:\\svn\\art\\Houdini\\HoudiniTool\\HexTool\\scripts\\python\\UEGui\\python\\Lib\\site-packages")

import assetsImportFromJson as ueim

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 142)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.callsheetpath = QtGui.QLineEdit(self.centralwidget)
        self.callsheetpath.setGeometry(QtCore.QRect(30, 20, 361, 20))
        self.callsheetpath.setObjectName("callsheetpath")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        self.menuImport_Assets = QtGui.QMenu(self.menubar)
        self.menuImport_Assets.setObjectName("menuImport_Assets")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuImport_Assets.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.ImportAssets)
    def ImportAssets(self):

        if os.path.exists(self.callsheetpath.text()):
            ueim.importMyAssets(self.callsheetpath.text())
        else:
            print "File Not Exists"

    def printMessage(self):
        print self.callsheetpath.text()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "ImportAssets", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImport_Assets.setTitle(QtGui.QApplication.translate("MainWindow", "Import Assets", None, QtGui.QApplication.UnicodeUTF8))




