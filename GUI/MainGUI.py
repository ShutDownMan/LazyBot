# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGUI.ui'
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

class Ui_BotMainWindow(object):
    def setupUi(self, BotMainWindow):
        BotMainWindow.setObjectName(_fromUtf8("BotMainWindow"))
        BotMainWindow.setEnabled(True)
        BotMainWindow.resize(677, 494)
        self.centralwidget = QtGui.QWidget(BotMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 671, 451))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Tabs = QtGui.QTabWidget(self.gridLayoutWidget)
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.GeneralTab = QtGui.QWidget()
        self.GeneralTab.setObjectName(_fromUtf8("GeneralTab"))
        self.AccountGB = QtGui.QGroupBox(self.GeneralTab)
        self.AccountGB.setGeometry(QtCore.QRect(10, 20, 291, 251))
        self.AccountGB.setObjectName(_fromUtf8("AccountGB"))
        self.AccountsTree = QtGui.QTreeWidget(self.AccountGB)
        self.AccountsTree.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.AccountsTree.setAlternatingRowColors(False)
        self.AccountsTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.AccountsTree.setObjectName(_fromUtf8("AccountsTree"))
        item_0 = QtGui.QTreeWidgetItem(self.AccountsTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_0 = QtGui.QTreeWidgetItem(self.AccountsTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        item_2 = QtGui.QTreeWidgetItem(item_1)
        self.AccountsTree.header().setCascadingSectionResizes(False)
        self.AccountsTree.header().setSortIndicatorShown(True)
        self.AccountsTree.header().setStretchLastSection(True)
        self.AddAccountBtn = QtGui.QPushButton(self.AccountGB)
        self.AddAccountBtn.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.AddAccountBtn.setObjectName(_fromUtf8("AddAccountBtn"))
        self.AddWorldBtn = QtGui.QPushButton(self.AccountGB)
        self.AddWorldBtn.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.AddWorldBtn.setObjectName(_fromUtf8("AddWorldBtn"))
        self.AddVillageBtn = QtGui.QPushButton(self.AccountGB)
        self.AddVillageBtn.setGeometry(QtCore.QRect(190, 220, 75, 23))
        self.AddVillageBtn.setObjectName(_fromUtf8("AddVillageBtn"))
        self.ActionsGB = QtGui.QGroupBox(self.GeneralTab)
        self.ActionsGB.setGeometry(QtCore.QRect(360, 20, 291, 401))
        self.ActionsGB.setObjectName(_fromUtf8("ActionsGB"))
        self.SetupBrowserBtn = QtGui.QPushButton(self.ActionsGB)
        self.SetupBrowserBtn.setGeometry(QtCore.QRect(10, 60, 91, 23))
        self.SetupBrowserBtn.setObjectName(_fromUtf8("SetupBrowserBtn"))
        self.OpenGameBtn = QtGui.QPushButton(self.ActionsGB)
        self.OpenGameBtn.setGeometry(QtCore.QRect(110, 60, 75, 23))
        self.OpenGameBtn.setObjectName(_fromUtf8("OpenGameBtn"))
        self.GameLbl = QtGui.QLabel(self.ActionsGB)
        self.GameLbl.setGeometry(QtCore.QRect(10, 40, 46, 13))
        self.GameLbl.setObjectName(_fromUtf8("GameLbl"))
        self.RallyPointLbl = QtGui.QLabel(self.ActionsGB)
        self.RallyPointLbl.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.RallyPointLbl.setObjectName(_fromUtf8("RallyPointLbl"))
        self.CloseWindowBtn = QtGui.QPushButton(self.ActionsGB)
        self.CloseWindowBtn.setGeometry(QtCore.QRect(190, 60, 91, 23))
        self.CloseWindowBtn.setObjectName(_fromUtf8("CloseWindowBtn"))
        self.SetupPredefsBtn = QtGui.QPushButton(self.ActionsGB)
        self.SetupPredefsBtn.setGeometry(QtCore.QRect(10, 150, 111, 23))
        self.SetupPredefsBtn.setObjectName(_fromUtf8("SetupPredefsBtn"))
        self.UpdatePredefsBtn = QtGui.QPushButton(self.ActionsGB)
        self.UpdatePredefsBtn.setGeometry(QtCore.QRect(140, 150, 121, 23))
        self.UpdatePredefsBtn.setObjectName(_fromUtf8("UpdatePredefsBtn"))
        self.BarbarianAttackerLbl = QtGui.QLabel(self.ActionsGB)
        self.BarbarianAttackerLbl.setGeometry(QtCore.QRect(10, 220, 101, 16))
        self.BarbarianAttackerLbl.setObjectName(_fromUtf8("BarbarianAttackerLbl"))
        self.SelectStrategy = QtGui.QComboBox(self.ActionsGB)
        self.SelectStrategy.setGeometry(QtCore.QRect(10, 250, 121, 22))
        self.SelectStrategy.setObjectName(_fromUtf8("SelectStrategy"))
        self.SelectStrategy.addItem(_fromUtf8(""))
        self.SelectStrategy.addItem(_fromUtf8(""))
        self.SelectStrategy.addItem(_fromUtf8(""))
        self.SelectStrategy.addItem(_fromUtf8(""))
        self.AttackStrategyModifierSpn = QtGui.QSpinBox(self.ActionsGB)
        self.AttackStrategyModifierSpn.setGeometry(QtCore.QRect(140, 250, 42, 22))
        self.AttackStrategyModifierSpn.setMinimum(-6)
        self.AttackStrategyModifierSpn.setMaximum(6)
        self.AttackStrategyModifierSpn.setObjectName(_fromUtf8("AttackStrategyModifierSpn"))
        self.ModifyAttackStrategyBtn = QtGui.QPushButton(self.ActionsGB)
        self.ModifyAttackStrategyBtn.setGeometry(QtCore.QRect(210, 250, 51, 23))
        self.ModifyAttackStrategyBtn.setObjectName(_fromUtf8("ModifyAttackStrategyBtn"))
        self.OneRoundAttackBtn = QtGui.QPushButton(self.ActionsGB)
        self.OneRoundAttackBtn.setGeometry(QtCore.QRect(160, 290, 101, 23))
        self.OneRoundAttackBtn.setObjectName(_fromUtf8("OneRoundAttackBtn"))
        self.VillageAttackLimitSpn = QtGui.QSpinBox(self.ActionsGB)
        self.VillageAttackLimitSpn.setGeometry(QtCore.QRect(10, 290, 91, 22))
        self.VillageAttackLimitSpn.setWrapping(False)
        self.VillageAttackLimitSpn.setMinimum(0)
        self.VillageAttackLimitSpn.setMaximum(9999)
        self.VillageAttackLimitSpn.setProperty("value", 2500)
        self.VillageAttackLimitSpn.setObjectName(_fromUtf8("VillageAttackLimitSpn"))
        self.LazyBotSheduleLbl = QtGui.QLabel(self.ActionsGB)
        self.LazyBotSheduleLbl.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.LazyBotSheduleLbl.setObjectName(_fromUtf8("LazyBotSheduleLbl"))
        self.ModifyLazyBotScheduleBtn = QtGui.QPushButton(self.ActionsGB)
        self.ModifyLazyBotScheduleBtn.setGeometry(QtCore.QRect(10, 360, 101, 23))
        self.ModifyLazyBotScheduleBtn.setObjectName(_fromUtf8("ModifyLazyBotScheduleBtn"))
        self.RunLazyBotScheduleBtn = QtGui.QPushButton(self.ActionsGB)
        self.RunLazyBotScheduleBtn.setGeometry(QtCore.QRect(130, 360, 101, 23))
        self.RunLazyBotScheduleBtn.setObjectName(_fromUtf8("RunLazyBotScheduleBtn"))
        self.UpdateWorldsBtn = QtGui.QPushButton(self.ActionsGB)
        self.UpdateWorldsBtn.setGeometry(QtCore.QRect(50, 90, 91, 23))
        self.UpdateWorldsBtn.setObjectName(_fromUtf8("UpdateWorldsBtn"))
        self.UpdateVillagesBtn = QtGui.QPushButton(self.ActionsGB)
        self.UpdateVillagesBtn.setGeometry(QtCore.QRect(150, 90, 91, 23))
        self.UpdateVillagesBtn.setObjectName(_fromUtf8("UpdateVillagesBtn"))
        self.BeCarefulLbl = QtGui.QLabel(self.ActionsGB)
        self.BeCarefulLbl.setGeometry(QtCore.QRect(80, 20, 141, 16))
        self.BeCarefulLbl.setObjectName(_fromUtf8("BeCarefulLbl"))
        self.line_2 = QtGui.QFrame(self.ActionsGB)
        self.line_2.setGeometry(QtCore.QRect(67, 120, 141, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.ActionsGB)
        self.line_3.setGeometry(QtCore.QRect(70, 200, 141, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.ActionsGB)
        self.line_4.setGeometry(QtCore.QRect(70, 320, 141, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.Action = QtGui.QPushButton(self.ActionsGB)
        self.Action.setGeometry(QtCore.QRect(80, 180, 101, 23))
        self.Action.setObjectName(_fromUtf8("Action"))
        self.line = QtGui.QFrame(self.GeneralTab)
        self.line.setGeometry(QtCore.QRect(320, 0, 20, 421))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.BotLogGB = QtGui.QGroupBox(self.GeneralTab)
        self.BotLogGB.setGeometry(QtCore.QRect(10, 280, 291, 121))
        self.BotLogGB.setObjectName(_fromUtf8("BotLogGB"))
        self.LazyBotLog = QtGui.QPlainTextEdit(self.BotLogGB)
        self.LazyBotLog.setGeometry(QtCore.QRect(10, 20, 271, 91))
        self.LazyBotLog.setObjectName(_fromUtf8("LazyBotLog"))
        self.Tabs.addTab(self.GeneralTab, _fromUtf8(""))
        self.AttacksTab = QtGui.QWidget()
        self.AttacksTab.setObjectName(_fromUtf8("AttacksTab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.AttacksTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 421))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.line_5 = QtGui.QFrame(self.horizontalLayoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.groupBox = QtGui.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.Tabs.addTab(self.AttacksTab, _fromUtf8(""))
        self.VillageTab = QtGui.QWidget()
        self.VillageTab.setObjectName(_fromUtf8("VillageTab"))
        self.Tabs.addTab(self.VillageTab, _fromUtf8(""))
        self.HeadQuarterTab = QtGui.QWidget()
        self.HeadQuarterTab.setSizeIncrement(QtCore.QSize(1, 0))
        self.HeadQuarterTab.setObjectName(_fromUtf8("HeadQuarterTab"))
        self.Tabs.addTab(self.HeadQuarterTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Tabs, 0, 0, 1, 1)
        BotMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BotMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuGeneral = QtGui.QMenu(self.menubar)
        self.menuGeneral.setObjectName(_fromUtf8("menuGeneral"))
        BotMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BotMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BotMainWindow.setStatusBar(self.statusbar)
        self.AddAccountAction = QtGui.QAction(BotMainWindow)
        self.AddAccountAction.setObjectName(_fromUtf8("AddAccountAction"))
        self.AddWorldAction = QtGui.QAction(BotMainWindow)
        self.AddWorldAction.setObjectName(_fromUtf8("AddWorldAction"))
        self.AddVillageAction = QtGui.QAction(BotMainWindow)
        self.AddVillageAction.setObjectName(_fromUtf8("AddVillageAction"))
        self.CloseAction = QtGui.QAction(BotMainWindow)
        self.CloseAction.setObjectName(_fromUtf8("CloseAction"))
        self.menuGeneral.addAction(self.AddAccountAction)
        self.menuGeneral.addAction(self.AddWorldAction)
        self.menuGeneral.addAction(self.AddVillageAction)
        self.menuGeneral.addSeparator()
        self.menuGeneral.addAction(self.CloseAction)
        self.menubar.addAction(self.menuGeneral.menuAction())

        self.retranslateUi(BotMainWindow)
        self.Tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.AddWorldBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.AddWorldDialog)
        QtCore.QObject.connect(self.AddVillageBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.AddVillageDialog)
        QtCore.QObject.connect(self.OneRoundAttackBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.RunOneRound)
        QtCore.QObject.connect(self.SetupBrowserBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.SetupBrowser)
        QtCore.QObject.connect(self.OpenGameBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallOpenGame)
        QtCore.QObject.connect(self.CloseWindowBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallCloseWindows)
        QtCore.QObject.connect(self.UpdateWorldsBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallUpdateWorlds)
        QtCore.QObject.connect(self.UpdateVillagesBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallUpdateVillages)
        QtCore.QObject.connect(self.SetupPredefsBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallSetupPredefinitions)
        QtCore.QObject.connect(self.UpdatePredefsBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallUpdatePredefinitions)
        QtCore.QObject.connect(self.Action, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallAction)
        QtCore.QObject.connect(self.ModifyAttackStrategyBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallModifyVillageAttackStrategy)
        QtCore.QObject.connect(self.ModifyLazyBotScheduleBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.ModifySchedule)
        QtCore.QObject.connect(self.RunLazyBotScheduleBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.CallRunSchedule)
        QtCore.QObject.connect(self.AddAccountBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), BotMainWindow.AddAccountDialog)
        QtCore.QObject.connect(self.AccountsTree, QtCore.SIGNAL(_fromUtf8("itemDoubleClicked(QTreeWidgetItem*,int)")), BotMainWindow.SubItemDoubleClick)
        QtCore.QObject.connect(self.AddAccountAction, QtCore.SIGNAL(_fromUtf8("triggered()")), BotMainWindow.AddAccountDialog)
        QtCore.QObject.connect(self.AddVillageAction, QtCore.SIGNAL(_fromUtf8("triggered()")), BotMainWindow.AddVillageDialog)
        QtCore.QObject.connect(self.AddWorldAction, QtCore.SIGNAL(_fromUtf8("triggered()")), BotMainWindow.AddWorldDialog)
        QtCore.QObject.connect(self.CloseAction, QtCore.SIGNAL(_fromUtf8("triggered()")), BotMainWindow.CloseWindow)
        QtCore.QMetaObject.connectSlotsByName(BotMainWindow)

    def retranslateUi(self, BotMainWindow):
        BotMainWindow.setWindowTitle(_translate("BotMainWindow", "LazyBot GUI", None))
        self.GeneralTab.setAccessibleName(_translate("BotMainWindow", "General", None))
        self.AccountGB.setTitle(_translate("BotMainWindow", "Account", None))
        self.AccountsTree.setToolTip(_translate("BotMainWindow", "Press Ctrl+Click to select multiple accounts/worlds/villages", None))
        self.AccountsTree.setSortingEnabled(True)
        self.AccountsTree.headerItem().setText(0, _translate("BotMainWindow", "Accounts", None))
        __sortingEnabled = self.AccountsTree.isSortingEnabled()
        self.AccountsTree.setSortingEnabled(False)
        self.AccountsTree.topLevelItem(0).setText(0, _translate("BotMainWindow", "Account2", None))
        self.AccountsTree.topLevelItem(0).child(0).setText(0, _translate("BotMainWindow", "World3", None))
        self.AccountsTree.topLevelItem(0).child(0).child(0).setText(0, _translate("BotMainWindow", "Village4", None))
        self.AccountsTree.topLevelItem(0).child(0).child(1).setText(0, _translate("BotMainWindow", "Village3", None))
        self.AccountsTree.topLevelItem(0).child(0).child(2).setText(0, _translate("BotMainWindow", "Village2", None))
        self.AccountsTree.topLevelItem(0).child(0).child(3).setText(0, _translate("BotMainWindow", "Village1", None))
        self.AccountsTree.topLevelItem(0).child(1).setText(0, _translate("BotMainWindow", "World2", None))
        self.AccountsTree.topLevelItem(0).child(1).child(0).setText(0, _translate("BotMainWindow", "Village2", None))
        self.AccountsTree.topLevelItem(0).child(1).child(1).setText(0, _translate("BotMainWindow", "Village1", None))
        self.AccountsTree.topLevelItem(0).child(2).setText(0, _translate("BotMainWindow", "World1", None))
        self.AccountsTree.topLevelItem(0).child(2).child(0).setText(0, _translate("BotMainWindow", "Village1", None))
        self.AccountsTree.topLevelItem(1).setText(0, _translate("BotMainWindow", "Account1", None))
        self.AccountsTree.topLevelItem(1).child(0).setText(0, _translate("BotMainWindow", "World2", None))
        self.AccountsTree.topLevelItem(1).child(0).child(0).setText(0, _translate("BotMainWindow", "Village2", None))
        self.AccountsTree.topLevelItem(1).child(0).child(1).setText(0, _translate("BotMainWindow", "Village1", None))
        self.AccountsTree.topLevelItem(1).child(1).setText(0, _translate("BotMainWindow", "World1", None))
        self.AccountsTree.topLevelItem(1).child(1).child(0).setText(0, _translate("BotMainWindow", "Village3", None))
        self.AccountsTree.topLevelItem(1).child(1).child(1).setText(0, _translate("BotMainWindow", "Village2", None))
        self.AccountsTree.topLevelItem(1).child(1).child(2).setText(0, _translate("BotMainWindow", "Village1", None))
        self.AccountsTree.setSortingEnabled(__sortingEnabled)
        self.AddAccountBtn.setToolTip(_translate("BotMainWindow", "Add account to list", None))
        self.AddAccountBtn.setText(_translate("BotMainWindow", "Add Account", None))
        self.AddWorldBtn.setToolTip(_translate("BotMainWindow", "Add world to account", None))
        self.AddWorldBtn.setText(_translate("BotMainWindow", "Add World", None))
        self.AddVillageBtn.setToolTip(_translate("BotMainWindow", "Add village to world", None))
        self.AddVillageBtn.setText(_translate("BotMainWindow", "Add Village", None))
        self.ActionsGB.setToolTip(_translate("BotMainWindow", "Actions are for SELECTED villages", None))
        self.ActionsGB.setTitle(_translate("BotMainWindow", "Actions", None))
        self.SetupBrowserBtn.setToolTip(_translate("BotMainWindow", "Opens Firefox broswer with game", None))
        self.SetupBrowserBtn.setText(_translate("BotMainWindow", "Setup Browser", None))
        self.OpenGameBtn.setToolTip(_translate("BotMainWindow", "Opens a browser per account and a tab per world", None))
        self.OpenGameBtn.setText(_translate("BotMainWindow", "Open Game", None))
        self.GameLbl.setText(_translate("BotMainWindow", "Game:", None))
        self.RallyPointLbl.setText(_translate("BotMainWindow", "Rally Point:", None))
        self.CloseWindowBtn.setToolTip(_translate("BotMainWindow", "Close all windows it opened", None))
        self.CloseWindowBtn.setText(_translate("BotMainWindow", "Close Window", None))
        self.SetupPredefsBtn.setToolTip(_translate("BotMainWindow", "Setup LazyBot\'s default predefinitions", None))
        self.SetupPredefsBtn.setText(_translate("BotMainWindow", "Setup Predefinitions", None))
        self.UpdatePredefsBtn.setToolTip(_translate("BotMainWindow", "Update predefinitions using unit ideal division", None))
        self.UpdatePredefsBtn.setText(_translate("BotMainWindow", "Update Predefinitions", None))
        self.BarbarianAttackerLbl.setText(_translate("BotMainWindow", "Barbarian Attacker:", None))
        self.SelectStrategy.setToolTip(_translate("BotMainWindow", "Select villages\' attack strategy", None))
        self.SelectStrategy.setItemText(0, _translate("BotMainWindow", "-- Attack Strategy --", None))
        self.SelectStrategy.setItemText(1, _translate("BotMainWindow", "Relatories", None))
        self.SelectStrategy.setItemText(2, _translate("BotMainWindow", "Competitive", None))
        self.SelectStrategy.setItemText(3, _translate("BotMainWindow", "Passive", None))
        self.AttackStrategyModifierSpn.setToolTip(_translate("BotMainWindow", "Add a modifier to selected attack strategy", None))
        self.ModifyAttackStrategyBtn.setToolTip(_translate("BotMainWindow", "Modify selected villages attack strategies", None))
        self.ModifyAttackStrategyBtn.setText(_translate("BotMainWindow", "Modify", None))
        self.OneRoundAttackBtn.setToolTip(_translate("BotMainWindow", "Do a 1 round attack to barbarians", None))
        self.OneRoundAttackBtn.setText(_translate("BotMainWindow", "One Round Attack!", None))
        self.VillageAttackLimitSpn.setToolTip(_translate("BotMainWindow", "Attack number limit per village in 12h", None))
        self.LazyBotSheduleLbl.setText(_translate("BotMainWindow", "LazyBot Schedule:", None))
        self.ModifyLazyBotScheduleBtn.setToolTip(_translate("BotMainWindow", "Modify village bot schedule", None))
        self.ModifyLazyBotScheduleBtn.setText(_translate("BotMainWindow", "Modify Schedule", None))
        self.RunLazyBotScheduleBtn.setToolTip(_translate("BotMainWindow", "Start bot for selected villages", None))
        self.RunLazyBotScheduleBtn.setText(_translate("BotMainWindow", "Run Schedule", None))
        self.UpdateWorldsBtn.setToolTip(_translate("BotMainWindow", "Update all worlds from account", None))
        self.UpdateWorldsBtn.setText(_translate("BotMainWindow", "Update Worlds", None))
        self.UpdateVillagesBtn.setToolTip(_translate("BotMainWindow", "Update all villages from account", None))
        self.UpdateVillagesBtn.setText(_translate("BotMainWindow", "Update Villages", None))
        self.BeCarefulLbl.setText(_translate("BotMainWindow", "Be careful with that section!", None))
        self.Action.setToolTip(_translate("BotMainWindow", "Setup LazyBot\'s default predefinitions", None))
        self.Action.setText(_translate("BotMainWindow", "Action", None))
        self.BotLogGB.setTitle(_translate("BotMainWindow", "Bot Log", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.GeneralTab), _translate("BotMainWindow", "General", None))
        self.groupBox_2.setTitle(_translate("BotMainWindow", "GroupBox", None))
        self.groupBox.setTitle(_translate("BotMainWindow", "GroupBox", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.AttacksTab), _translate("BotMainWindow", "Attacks", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.VillageTab), _translate("BotMainWindow", "Village", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.HeadQuarterTab), _translate("BotMainWindow", "Headquarter", None))
        self.menuGeneral.setTitle(_translate("BotMainWindow", "General", None))
        self.AddAccountAction.setText(_translate("BotMainWindow", "Add account", None))
        self.AddAccountAction.setToolTip(_translate("BotMainWindow", "Add account to tree", None))
        self.AddAccountAction.setShortcut(_translate("BotMainWindow", "Ctrl+N", None))
        self.AddWorldAction.setText(_translate("BotMainWindow", "Add World", None))
        self.AddWorldAction.setToolTip(_translate("BotMainWindow", "Add World to account", None))
        self.AddVillageAction.setText(_translate("BotMainWindow", "Add Village", None))
        self.AddVillageAction.setToolTip(_translate("BotMainWindow", "Add Village to world", None))
        self.CloseAction.setText(_translate("BotMainWindow", "Close", None))
        self.CloseAction.setShortcut(_translate("BotMainWindow", "Ctrl+W", None))

