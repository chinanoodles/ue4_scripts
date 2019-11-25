# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputcallSheetLable.ui'
#
# Created: Tue Nov  5 15:29:13 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import getpass
import ue_call_sheet
reload(ue_call_sheet)

USER = getpass.getuser()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 171)

        self.callSheetLineEdit = QtGui.QLineEdit(Dialog)
        self.callSheetLineEdit.setGeometry(QtCore.QRect(160, 50, 571, 31))
        self.callSheetLineEdit.setObjectName("callSheetLineEdit")

        self.callSheetLable = QtGui.QLabel(Dialog)
        self.callSheetLable.setGeometry(QtCore.QRect(30, 50, 100, 31))
        self.callSheetLable.setObjectName("callSheetLablePath")


        self.fbxLineEdit = QtGui.QLineEdit(Dialog)
        self.fbxLineEdit.setGeometry(QtCore.QRect(160, 80, 571, 31))
        self.fbxLineEdit.setObjectName("fbxLineEdit")

        self.fbxPathLable = QtGui.QLabel(Dialog)
        self.fbxPathLable.setGeometry(QtCore.QRect(30, 80, 100, 31))
        self.fbxPathLable.setObjectName("fbxPathLable")



        self.ExportcallSheetLable = QtGui.QPushButton(Dialog)
        self.ExportcallSheetLable.setGeometry(QtCore.QRect(610, 130, 75, 23))
        self.ExportcallSheetLable.setObjectName("ExportcallSheetLable")

        self.retranslateUi(Dialog)
        self.ExportcallSheetLable.clicked.connect(self.exportClick)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        path = "C:\\Users\\{USER}\\Documents\\tst.json".format(USER = USER)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.callSheetLineEdit.setText(QtGui.QApplication.translate("Dialog", path, None, QtGui.QApplication.UnicodeUTF8))

        self.fbxLineEdit.setText(QtGui.QApplication.translate("Dialog", path, None, QtGui.QApplication.UnicodeUTF8))

        self.callSheetLable.setText(QtGui.QApplication.translate("Dialog", "Callsheet Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fbxPathLable.setText(QtGui.QApplication.translate("Dialog", "FBX Output Path", None, QtGui.QApplication.UnicodeUTF8))

        self.ExportcallSheetLable.setText(QtGui.QApplication.translate("Dialog", "Export", None, QtGui.QApplication.UnicodeUTF8))


    def exportClick(self):
        callsheet_path = self.callSheetLineEdit.text()
        fbx_path = self.fbxLineEdit.text()
        a = ue_call_sheet
        a.output(callsheet_path,fbx_path)


        print self.callSheetLineEdit.text()



