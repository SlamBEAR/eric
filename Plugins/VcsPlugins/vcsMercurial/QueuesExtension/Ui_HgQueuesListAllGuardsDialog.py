# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Plugins/VcsPlugins/vcsMercurial/QueuesExtension/HgQueuesListAllGuardsDialog.ui'
#
# Created: Tue Nov 18 17:53:57 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesListAllGuardsDialog(object):
    def setupUi(self, HgQueuesListAllGuardsDialog):
        HgQueuesListAllGuardsDialog.setObjectName("HgQueuesListAllGuardsDialog")
        HgQueuesListAllGuardsDialog.resize(400, 400)
        HgQueuesListAllGuardsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgQueuesListAllGuardsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.guardsTree = QtWidgets.QTreeWidget(HgQueuesListAllGuardsDialog)
        self.guardsTree.setAlternatingRowColors(True)
        self.guardsTree.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.guardsTree.setHeaderHidden(True)
        self.guardsTree.setObjectName("guardsTree")
        self.guardsTree.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.guardsTree)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesListAllGuardsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesListAllGuardsDialog)
        self.buttonBox.accepted.connect(HgQueuesListAllGuardsDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesListAllGuardsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesListAllGuardsDialog)
        HgQueuesListAllGuardsDialog.setTabOrder(self.guardsTree, self.buttonBox)

    def retranslateUi(self, HgQueuesListAllGuardsDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesListAllGuardsDialog.setWindowTitle(_translate("HgQueuesListAllGuardsDialog", "List All Guards"))
        self.guardsTree.setToolTip(_translate("HgQueuesListAllGuardsDialog", "Show all guards of all patches"))

