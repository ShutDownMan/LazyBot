# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#import wx
import os

#from LazyBotGUI import MainFrame
from classes.commands import Commands
from classes.dom import DOM
from classes.build_upgrader import Build_Upgrader
from classes.globe_map import Globe_Map
from classes.file_utils import File_Utils
from classes.game import Game
from classes.rallypoint import RallyPoint
from classes.get_all_barbs import UpdateBarbarianList
from classes.barbarian_attacker import BarbarianAttacker
from classes.resource_gather import Resource_Gather

class VillageController():
	firefox_capabilities = None	# Needed to setup browser
	foxDriver = None			# Browser selenium driver
	page = None					# Module related to selenium elements
	cmd = None					# Module with main game commands
	upgrader = None				# Module with HeadQuarter related commands
	globe_map = None			# Module with coord searching related commands
	ufile = None				# Module with file related functions
	game = None					# Module with misc game related commands
	rallypoint = None			# Module with Rally Point related commands
	barblist_updater = None		# Module with
	barbattacker = None			# Module with farming related commands
	resource_gather = None		# Module with farming related commands

	current_account = ''		# Store 
	current_world = ''			# Store 
	current_village = '0x00 - Village'		# Store 
	current_attacks = None		# Store all current logged attacks

	account_status = None		# Store 
	world_status = None			# Store 
	village_status = None		# Store 
	all_barbarians = None		# Store 

	Bot_Dir = os.getcwd()
	Units_Stats = None
	Barbarians_Map = None

	def __init__(self):
		self.cmd = Commands(self)
		self.page = DOM(self)
		self.game = Game(self)
		self.ufile = File_Utils(self)
		self.upgrader = Build_Upgrader(self)
		self.globe_map = Globe_Map(self)
		self.rallypoint = RallyPoint(self)
		self.barbattacker = BarbarianAttacker(self)
		self.resource_gather = Resource_Gather(self)
		self.barblist_updater = UpdateBarbarianList(self)

		self.account_status = self.ufile.get_account_status()
		self.world_status = self.ufile.get_world_status()
		self.village_status = self.ufile.get_village_status()

		self.all_barbarians = self.ufile.get_config('World Barbarians List')
		self.Units_Stats = self.ufile.get_config('Units Stats')
		self.Barbarians_Map = self.ufile.get_config('Barbarian Maps')


	def start_schedule(self):
		for stats, value in self.world_status.items():
			if 'Village' in value:
				self.game.select_game()
				self.current_village = stats
				self.globe_map.Search_Coords()
			#	self.resource_gather.gather_resources()
				self.upgrader.check_build_schedule()
				self.upgrader.check_build_schedule()
				self.rallypoint.predefiniton_setup()
				# run schedule for village
		self.game.wait(3)
	#	self.start_schedule()
		pass


	def update_vars(self):
		self.Barbarians_Map = self.ufile.get_config('Barbarian Maps')

		self.account_status = self.ufile.get_account_status()
		print self.account_status
		self.world_status = self.ufile.get_world_status()
		print self.world_status
		self.village_status = self.ufile.get_village_status()
		print self.village_status


if __name__ == "__main__":
#	app = wx.App(False)
#	frame = MainFrame(parent=None)
#	frame.Show()
#	app.MainLoop()
#	bot = LazyBot()
	pass
