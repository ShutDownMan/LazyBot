# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PyQt4 import QtCore, QtGui, uic

import sys

from MainGUI import Ui_BotMainWindow
from AccountDialog import Ui_AccountDialog
from WorldDialog import Ui_WorldDialog
from VillageDialog import Ui_VillageDialog

class MainWindow(QtGui.QMainWindow, Ui_BotMainWindow):

	SelectedItems = None

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.mainUI = Ui_BotMainWindow()
		self.mainUI.setupUi(self)

	def AddAccountDialog(self):
		print "AddAccountDialog()"
		window = AccountDialog(self)
		window.show()
		pass

	def AddWorldDialog(self):
		print "AddWorldDialog()"
		window = WorldDialog(self)
		window.show()
		pass

	def AddVillageDialog(self):
		print "AddVillageDialog()"
		window = WorldDialog(self)
		window.show()
		pass

	def RunOneRound(self):
		print "RunOneRound()"
		pass

	def SetupBrowser(self):
		print "SetupBrowser()"
		pass

	def CallOpenGame(self):
		print "CallOpenGame()"
		pass

	def CallCloseWindows(self):
		print "CallCloseWindows()"
		pass

	def CallUpdateWorlds(self):
		print "CallUpdateWorlds()"
		pass

	def CallUpdateVillages(self):
		print "CallUpdateVillages()"
		pass

	def CallSetupPredefinitions(self):
		print "CallSetupPredefinitions()"
		pass

	def CallUpdatePredefinitions(self):
		print "CallUpdatePredefinitions()"
		pass

	def CallModifyVillageAttackStrategy(self):
		print "CallModifyVillageAttackStrategy()"
		pass

	def ModifySchedule(self):
		print "ModifySchedule()"
		pass

	def CallRunSchedule(self):
		print "CallRunSchedule()"
		pass

	def SubItemDoubleClick(self, *items):
		print "SubItemDoubleClick()"
		itemList = self.mainUI.AccountsTree.selectedItems()
		for i, item in enumerate(itemList):
			print item.text(i)
	#	self.mainUI.Tabs.setFocus(0)
		pass

	def CloseWindow(self):
		print "CloseWindow()"
		self.close()
		pass

	def UpdateSelectedItems(self):
		print "UpdateSelectedItems()"
		self.SelectedItems = self.mainUI.AccountsTree.selectedItems()
		pass

	def CallAction(self):
		print "CallAction()"
		pass


class AccountDialog(QtGui.QDialog, Ui_AccountDialog):

	def __init__(self, parent=None):
		super(AccountDialog, self).__init__(parent)
		self.ui = Ui_AccountDialog()
		self.ui.setupUi(self)

	def accept(self):
		print "accept()"
		username = self.ui.UsernameInput.text()
		password = self.ui.PasswordInput.text()
		args = [username, password]
		self.close()
		print args
		# use args to create dirs and status
		pass


class WorldDialog(QtGui.QDialog, Ui_WorldDialog):

	def __init__(self, parent=None):
		super(WorldDialog, self).__init__(parent)
		self.ui = Ui_WorldDialog()
		self.ui.setupUi(self)

	def accept(self):
		print "accept()"
		world = self.ui.WorldInput.text()
		self.close()
		args = [world]
		print args
		# use args to create dirs and status
		pass


class VillageDialog(QtGui.QDialog, Ui_VillageDialog):

	def __init__(self, parent=None):
		super(VillageDialog, self).__init__(parent)
		self.ui = Ui_VillageDialog()
		self.ui.setupUi(self)

	def accept(self):
		print "accept()"
		village = self.ui.VillageInput.text()
		self.close()
		args = [village]
		print args
		# use args to create dirs and status
		pass

if __name__ == '__main__':     
	app = QtGui.QApplication(sys.argv)
	myW = MainWindow()
	myW.show()
	sys.exit(app.exec_())
