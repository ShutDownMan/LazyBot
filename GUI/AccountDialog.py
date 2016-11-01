# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'AccountDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AccountDialog(object):
    def setupUi(self, AccountDialog):
        AccountDialog.setObjectName(_fromUtf8("AccountDialog"))
        AccountDialog.resize(400, 129)
        self.DialogBtn = QtGui.QDialogButtonBox(AccountDialog)
        self.DialogBtn.setGeometry(QtCore.QRect(30, 80, 341, 32))
        self.DialogBtn.setOrientation(QtCore.Qt.Horizontal)
        self.DialogBtn.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.DialogBtn.setObjectName(_fromUtf8("DialogBtn"))
        self.UsernameInput = QtGui.QLineEdit(AccountDialog)
        self.UsernameInput.setGeometry(QtCore.QRect(20, 40, 151, 20))
        self.UsernameInput.setObjectName(_fromUtf8("UsernameInput"))
        self.label = QtGui.QLabel(AccountDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AccountDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PasswordInput = QtGui.QLineEdit(AccountDialog)
        self.PasswordInput.setGeometry(QtCore.QRect(190, 40, 151, 20))
        self.PasswordInput.setObjectName(_fromUtf8("PasswordInput"))

        self.retranslateUi(AccountDialog)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("accepted()")), AccountDialog.accept)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("rejected()")), AccountDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountDialog)
        AccountDialog.setTabOrder(self.UsernameInput, self.PasswordInput)
        AccountDialog.setTabOrder(self.PasswordInput, self.DialogBtn)

    def retranslateUi(self, AccountDialog):
        AccountDialog.setWindowTitle(_translate("AccountDialog", "Dialog", None))
        self.label.setText(_translate("AccountDialog", "Username:", None))
        self.label_2.setText(_translate("AccountDialog", "Password:", None))

