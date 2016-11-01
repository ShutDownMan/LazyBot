# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VillageDialog.ui'
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

class Ui_VillageDialog(object):
    def setupUi(self, VillageDialog):
        VillageDialog.setObjectName(_fromUtf8("VillageDialog"))
        VillageDialog.resize(225, 115)
        self.label = QtGui.QLabel(VillageDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.DialogBtn = QtGui.QDialogButtonBox(VillageDialog)
        self.DialogBtn.setGeometry(QtCore.QRect(20, 80, 171, 32))
        self.DialogBtn.setOrientation(QtCore.Qt.Horizontal)
        self.DialogBtn.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.DialogBtn.setObjectName(_fromUtf8("DialogBtn"))
        self.VillageInput = QtGui.QLineEdit(VillageDialog)
        self.VillageInput.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.VillageInput.setObjectName(_fromUtf8("VillageInput"))

        self.retranslateUi(VillageDialog)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("accepted()")), VillageDialog.accept)
        QtCore.QObject.connect(self.DialogBtn, QtCore.SIGNAL(_fromUtf8("rejected()")), VillageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VillageDialog)

    def retranslateUi(self, VillageDialog):
        VillageDialog.setWindowTitle(_translate("VillageDialog", "Add Village", None))
        self.label.setText(_translate("VillageDialog", "Village name:", None))

