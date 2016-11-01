# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorldDialog.ui'
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

class Ui_WorldDialog(object):
    def setupUi(self, WorldDialog):
        WorldDialog.setObjectName(_fromUtf8("WorldDialog"))
        WorldDialog.resize(225, 115)
        self.WorldInput = QtGui.QLineEdit(WorldDialog)
        self.WorldInput.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.WorldInput.setObjectName(_fromUtf8("WorldInput"))
        self.DialogBtn = QtGui.QDialogButtonBox(WorldDialog)
        self.DialogBtn.setGeometry(QtCore.QRect(40, 80, 171, 32))
        self.DialogBtn.setOrientation(QtCore.Qt.Horizontal)
        self.DialogBtn.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.DialogBtn.setObjectName(_fromUtf8("DialogBtn"))
        self.label = QtGui.QLabel(WorldDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(WorldDialog)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("accepted()")), WorldDialog.accept)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("rejected()")), WorldDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WorldDialog)

    def retranslateUi(self, WorldDialog):
        WorldDialog.setWindowTitle(_translate("WorldDialog", "Add World", None))
        self.label.setText(_translate("WorldDialog", "World Name:", None))

