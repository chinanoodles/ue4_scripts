# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputcallSheetLable.ui'
#
# Created: Tue Nov  5 15:29:13 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import getpass
import ueAssets
reload(ueAssets)

USER = getpass.getuser()

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtGui.QMainWindow()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(788, 171)

    def setupUi(self):


        self.callSheetLineEdit = QtGui.QLineEdit(self.Dialog)
        self.callSheetLineEdit.setGeometry(QtCore.QRect(160, 50, 440, 30))
        self.callSheetLineEdit.setObjectName("callSheetLineEdit")

        self.callSheetBrowser = QtGui.QPushButton(self.Dialog)
        self.callSheetBrowser.setGeometry(QtCore.QRect(610, 50, 30, 30))
        self.callSheetBrowser.setObjectName("callSheetBrowser")

        self.callSheetLable = QtGui.QLabel(self.Dialog)
        self.callSheetLable.setGeometry(QtCore.QRect(30, 50, 100, 30))
        self.callSheetLable.setObjectName("callSheetLablePath")


        self.fbxLineEdit = QtGui.QLineEdit(self.Dialog)
        self.fbxLineEdit.setGeometry(QtCore.QRect(160, 80, 440, 30))
        self.fbxLineEdit.setObjectName("fbxLineEdit")

        self.fbxBrowser = QtGui.QPushButton(self.Dialog)
        self.fbxBrowser.setGeometry(QtCore.QRect(610, 80, 30, 30))
        self.fbxBrowser.setObjectName("fbxBrowser")

        self.fbxPathLable = QtGui.QLabel(self.Dialog)
        self.fbxPathLable.setGeometry(QtCore.QRect(30, 80, 100, 30))
        self.fbxPathLable.setObjectName("fbxPathLable")



        self.ExportcallSheetLable = QtGui.QPushButton(self.Dialog)
        self.ExportcallSheetLable.setGeometry(QtCore.QRect(610, 130, 75, 23))
        self.ExportcallSheetLable.setObjectName("ExportcallSheetLable")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.ExportcallSheetLable.clicked.connect(self.exportClick)

        self.callSheetBrowser.clicked.connect(self.openCallSheetBrowser)
        self.fbxBrowser.clicked.connect(self.openfbxBrowser)

        

    def retranslateUi(self):
        path = "C:\\Users\\{USER}\\Documents\\tst.json".format(USER = USER)
        fbxpath = "C:\\Users\\{USER}\\Documents\\".format(USER = USER)
        self.Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.callSheetLineEdit.setText(QtGui.QApplication.translate("Dialog", path, None, QtGui.QApplication.UnicodeUTF8))
        self.callSheetBrowser.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.fbxLineEdit.setText(QtGui.QApplication.translate("Dialog", fbxpath, None, QtGui.QApplication.UnicodeUTF8))
        self.fbxBrowser.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.callSheetLable.setText(QtGui.QApplication.translate("Dialog", "Callsheet Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fbxPathLable.setText(QtGui.QApplication.translate("Dialog", "FBX Output Path", None, QtGui.QApplication.UnicodeUTF8))

        self.ExportcallSheetLable.setText(QtGui.QApplication.translate("Dialog", "Export", None, QtGui.QApplication.UnicodeUTF8))

    def openCallSheetBrowser(self):
        filename, filter = QtGui.QFileDialog.getSaveFileName(parent = self.Dialog,caption='Open file', dir='.', filter='Call Sheet Files (*.json)')
        self.callSheetLineEdit.setText( filename )

        print filename
    def openfbxBrowser(self):
        flodername = QtGui.QFileDialog.getExistingDirectory(parent = self.Dialog,caption='Output fbx folder', dir='.')
        self.fbxLineEdit.setText( flodername + "/" )

        print flodername

    def exportClick(self):

        lib = ueAssets.hex_assets()
        lib.setfbxPath(self.fbxLineEdit.text())
        lib.setCallsheetPath(self.callSheetLineEdit.text())

        lib.getSelectedAssets()
        lib.setData()

        lib.exportJson()
        lib.exportFbx()


        print self.callSheetLineEdit.text()



