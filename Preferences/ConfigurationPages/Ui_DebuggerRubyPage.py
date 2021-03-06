# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Preferences/ConfigurationPages/DebuggerRubyPage.ui'
#
# Created: Tue Nov 18 17:53:56 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebuggerRubyPage(object):
    def setupUi(self, DebuggerRubyPage):
        DebuggerRubyPage.setObjectName("DebuggerRubyPage")
        DebuggerRubyPage.resize(400, 170)
        self.vboxlayout = QtWidgets.QVBoxLayout(DebuggerRubyPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(DebuggerRubyPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line11_2_2 = QtWidgets.QFrame(DebuggerRubyPage)
        self.line11_2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11_2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11_2_2.setObjectName("line11_2_2")
        self.vboxlayout.addWidget(self.line11_2_2)
        self.groupBox = QtWidgets.QGroupBox(DebuggerRubyPage)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName("hboxlayout")
        self.rubyInterpreterEdit = QtWidgets.QLineEdit(self.groupBox)
        self.rubyInterpreterEdit.setObjectName("rubyInterpreterEdit")
        self.hboxlayout.addWidget(self.rubyInterpreterEdit)
        self.rubyInterpreterButton = QtWidgets.QToolButton(self.groupBox)
        self.rubyInterpreterButton.setObjectName("rubyInterpreterButton")
        self.hboxlayout.addWidget(self.rubyInterpreterButton)
        self.vboxlayout.addWidget(self.groupBox)
        self.rbRedirectCheckBox = QtWidgets.QCheckBox(DebuggerRubyPage)
        self.rbRedirectCheckBox.setObjectName("rbRedirectCheckBox")
        self.vboxlayout.addWidget(self.rbRedirectCheckBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(DebuggerRubyPage)
        QtCore.QMetaObject.connectSlotsByName(DebuggerRubyPage)

    def retranslateUi(self, DebuggerRubyPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("DebuggerRubyPage", "<b>Configure Ruby Debugger</b>"))
        self.groupBox.setTitle(_translate("DebuggerRubyPage", "Ruby Interpreter for Debug Client"))
        self.rubyInterpreterEdit.setToolTip(_translate("DebuggerRubyPage", "Enter the path of the Ruby interpreter to be used by the debug client."))
        self.rubyInterpreterButton.setToolTip(_translate("DebuggerRubyPage", "Press to select the Ruby interpreter via a file selection dialog"))
        self.rbRedirectCheckBox.setToolTip(_translate("DebuggerRubyPage", "Select, to redirect stdin, stdout and stderr of the program being debugged to the eric6 IDE"))
        self.rbRedirectCheckBox.setText(_translate("DebuggerRubyPage", "Redirect stdin/stdout/stderr"))

