

#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the PySide examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

"""PySide2 port of the widgets/dialogs/findfiles example from Qt v5.x"""

from PySide2 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.browseButton = self.createButton("&Browse...", self.browse)
        self.findButton = self.createButton("&Export", self.tst)
        self.importButton = self.createButton("&Import", self.tst)
        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())

        directoryLabel = QtWidgets.QLabel("callsheet:")
        self.filesFoundLabel = QtWidgets.QLabel()

        self.callsheet =""
        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(self.findButton)
        buttonsLayout.addWidget(self.importButton)

        mainLayout = QtWidgets.QGridLayout()

        mainLayout.addWidget(directoryLabel, 2, 0)
        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(self.browseButton, 2, 2)

        mainLayout.addLayout(buttonsLayout, 5, 0, 1, 3)

        self.setLayout(mainLayout)

        self.setWindowTitle("CallSheet")
        self.resize(500, 300)

    def browse(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "CallSheet",
                QtCore.QDir.currentPath(),filter="*.json")
        my_file = Path(file_path[0])
        print(file_path[0])
        if my_file.exists():
            self.directoryComboBox.insertItems(0,file_path)
            self.directoryComboBox.setCurrentIndex(0)
            self.callsheet = file_path[0]

    def createButton(self, text, member):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, text=""):
        comboBox = QtWidgets.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Preferred)
        return comboBox

    def makedir(self):
        dir_path = os.path.dirname(os.path.realpath(self.callsheet))
        base = os.path.basename(self.callsheet)
        folder_name = os.path.splitext(base)[0]
        path = dir_path+"/"+folder_name
        os.makedirs(folder_name, mode = 0o777, exist_ok = True) 
        return folder_name
    def tst(self):
        
         print(self.directoryComboBox.currentText())


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
