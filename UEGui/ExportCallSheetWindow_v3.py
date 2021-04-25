
#############################################################################
##
##
## if there is any problem. feel free to contact zhangfan05@corp.netease.com
##
##
#############################################################################

from PySide2 import QtCore, QtGui, QtWidgets
import os
import ueAssets
from imp import reload
reload(ueAssets)

import pyperclip



class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # env vars
        self.outputpath = os.getenv("OUTPUT")

        self.browseButton = self.createButton("&Browse...", self.browse)
        self.findButton = self.createButton("&Find", self.find)
        self.exportButton = self.createButton("&Export", self.exportClick)
        self.importButton = self.createButton("&Import", self.importClick)
        self.fileComboBox = self.createComboBox("Callsheet_tst")
        self.directoryComboBox = self.createComboBox(os.getenv("OUTPUT"))



        fileLabel = QtWidgets.QLabel("Callsheet Named:")

        directoryLabel = QtWidgets.QLabel("Callsheet Directory:")
        self.filesFoundLabel = QtWidgets.QLabel()

        self.createFilesTable()

        self.type = QtWidgets.QCheckBox()
        self.type.setText("Particles System")
        self.type.setChecked(False)

        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(self.findButton)
        buttonsLayout.addWidget(self.exportButton)
        buttonsLayout.addWidget(self.importButton)

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(fileLabel, 0, 0)
        mainLayout.addWidget(self.fileComboBox, 0, 1, 1, 2)

        mainLayout.addWidget(directoryLabel, 2, 0)
        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(self.browseButton, 2, 2)
        mainLayout.addWidget(self.filesTable, 3, 0, 1, 3)
        mainLayout.addWidget(self.filesFoundLabel, 4, 0)
        mainLayout.addWidget(self.type, 5, 0)
        mainLayout.addLayout(buttonsLayout, 5, 1, 2, 3)
        
        self.setLayout(mainLayout)

        self.setWindowTitle("Instance Callsheet IO")
        self.resize(500, 300)

        self.callsheet_path = None
    def browse(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    @staticmethod
    def updateComboBox(comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    def find(self):
        self.filesTable.setRowCount(0)

        fileName = self.fileComboBox.currentText()

        path = self.directoryComboBox.currentText()

        self.updateComboBox(self.fileComboBox)

        self.updateComboBox(self.directoryComboBox)

        self.currentDir = QtCore.QDir(path)
        fileName = "*.json"
        files = self.currentDir.entryList([fileName],
                QtCore.QDir.Files | QtCore.QDir.NoSymLinks)
        self.showFiles(files)

        

    def findFiles(self, files, text):
        progressDialog = QtWidgets.QProgressDialog(self)

        progressDialog.setCancelButtonText("&Cancel")
        progressDialog.setRange(0, len(files))
        progressDialog.setWindowTitle("Find Files")

        foundFiles = []

        for i in range(len(files)):
            progressDialog.setValue(i)
            progressDialog.setLabelText("Searching file number %d of %d..." % (i, len(files)))
            QtCore.qApp.processEvents()

            if progressDialog.wasCanceled():
                break

            inFile = QtCore.QFile(self.currentDir.absoluteFilePath(files[i]))

            if inFile.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(inFile)
                while not stream.atEnd():
                    if progressDialog.wasCanceled():
                        break
                    line = stream.readLine()
                    if text in line:
                        foundFiles.append(files[i])
                        break

        progressDialog.close()

        return foundFiles

    def showFiles(self, files):
        for fn in files:
            file = QtCore.QFile(self.currentDir.absoluteFilePath(fn))
            size = QtCore.QFileInfo(file).size()
            date =  QtCore.QFileInfo(file).lastModified()

            fileNameItem = QtWidgets.QTableWidgetItem(fn)
            fileNameItem.setFlags(fileNameItem.flags() ^ QtCore.Qt.ItemIsEditable)
            sizeItem = QtWidgets.QTableWidgetItem("%d KB" % (int((size + 1023) / 1024)))
            sizeItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            sizeItem.setFlags(sizeItem.flags() ^ QtCore.Qt.ItemIsEditable)

            dateItem = QtWidgets.QTableWidgetItem( date.toString() )
            dateItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            dateItem.setFlags(dateItem.flags() ^ QtCore.Qt.ItemIsEditable)

            row = self.filesTable.rowCount()
            self.filesTable.insertRow(row)
            self.filesTable.setItem(row, 0, fileNameItem)
            self.filesTable.setItem(row, 1, sizeItem)
            self.filesTable.setItem(row, 2, dateItem)

        self.filesFoundLabel.setText("%d file(s) found (Double click on a file to open it)" % len(files))

    def createButton(self, text, member):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, text=""):
        comboBox = QtWidgets.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.addItem("Q:\Project\output\H72\zhangfan05\callsheet_4.26")
        
        comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Preferred)
        return comboBox

    def createFilesTable(self):
        self.filesTable = QtWidgets.QTableWidget(0, 3)
        self.filesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.filesTable.setHorizontalHeaderLabels(("File Name", "Size","Date"))
        self.filesTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid(True)

        self.filesTable.cellActivated.connect(self.openFileOfItem)
        

    def openFileOfItem(self, row, column):
        item = self.filesTable.item(row, 0)

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.currentDir.absoluteFilePath(item.text())))
    def exportClick(self):
        print("export")

        fileName = self.fileComboBox.currentText()
        if self.type.isChecked():
            print("particles")

            print(fileName)
        else:
            print("meshes")
            #lib = ueAssets.hex_assets()
            # mkdir of fbx and export fbx
            dir_path = self.directoryComboBox.currentText()
            callsheet_path = dir_path +"/"+ fileName+".json"
            dir_path =dir_path +"/"+ fileName 
            os.makedirs(dir_path, mode = 0o777, exist_ok = True)
            self.callsheet_path = callsheet_path
            print(dir_path)
            #export callsheet
            lib = ueAssets.hex_assets()
            lib.setfbxPath(dir_path)

            lib.setCallsheetPath(callsheet_path)
            lib.getSelectedAssets()
            
            lib.setData()

            lib.exportJson()
            lib.exportFbx()
            self.informationMessage()
    def importClick(self):
        print("import")
        item = self.filesTable.currentItem()
        if item == None:
            print(item)
        else:
            print("import")
            json_path = self.currentDir.absoluteFilePath(item.text())
            print(json_path)
            lib = ueAssets.hex_assets()
            lib.setUeAsset_path("/Game/AutoImport/")
            lib.setCallsheetPath(json_path)
            lib.importMyAssets()
            print("finished")

    def informationMessage(self):    
        reply = QtWidgets.QMessageBox.information(self,
                "Callsheet Has been generated:", self.callsheet_path)
        if reply == QtWidgets.QMessageBox.Ok:
            pyperclip.copy(self.callsheet_path)
            spam = pyperclip.paste()
        else:
            pass
if __name__ == '__main__':

    import sys
    import threading

    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
	    app = QtWidgets.QApplication.instance()
    window = Window()
    window.show()
    t = threading.Thread(target = lambda: app.exec_())
    #t.daemon = True
	#t.start()
    print("App freezes the main process!")
