# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/AddFoundFilesDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFoundFilesDialog(object):
    def setupUi(self, AddFoundFilesDialog):
        AddFoundFilesDialog.setObjectName("AddFoundFilesDialog")
        AddFoundFilesDialog.resize(600, 480)
        AddFoundFilesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(AddFoundFilesDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.fileList = QtWidgets.QListWidget(AddFoundFilesDialog)
        self.fileList.setAlternatingRowColors(True)
        self.fileList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.fileList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fileList.setObjectName("fileList")
        self.vboxlayout.addWidget(self.fileList)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddFoundFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AddFoundFilesDialog)
        self.buttonBox.rejected.connect(AddFoundFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFoundFilesDialog)

    def retranslateUi(self, AddFoundFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        AddFoundFilesDialog.setWindowTitle(_translate("AddFoundFilesDialog", "Add found files to project"))
        AddFoundFilesDialog.setToolTip(_translate("AddFoundFilesDialog", "Adds the found files to the current project."))
        self.fileList.setToolTip(_translate("AddFoundFilesDialog", "List of found files."))

