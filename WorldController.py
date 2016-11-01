# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from selenium.webdriver.common.keys import Keys

from VillageController import VillageController

class WorldController():

	account = None

	controller = None

	tabs = {}

	def __init__(self, account):
		self.controller = VillageController()
		self.controller.current_account = account
		self.account = account
		self.start_bot()
		

	def start_bot(self):
		self.controller.cmd.setupBrowser()
		self.open_world("Poenari")
		self.controller.foxDriver.close()
		self.run_through_worlds(self.tabs)
	#	self.cmd.log_in(self.account_status['Username'],self.account_status['Password'])
	#	start a loop

	def open_world(self, world_name):
		driver = self.controller.foxDriver
		# //Get the current window handle
		first_tab = driver.current_window_handle;

		# find topmost element
		element = driver.find_element_by_tag_name('html')

		# Create new tab
		element.send_keys(Keys.CONTROL + 't')

		# //Get the list of window handles
		cur_tabs = driver.window_handles;

		new_tab = cur_tabs[len(cur_tabs)-1]
		print first_tab, ' ----- ', new_tab

		print len(cur_tabs);
		# //Use the list of window handles to switch between windows
		driver.switch_to_window(first_tab);
	#	controller.cmd.log_in(controller.account_status['Username'],controller.account_status['Password'])

		self.tabs.update({world_name:new_tab})

		return new_tab



	def run_through_worlds(self, tabs):
		controller = self.controller
		driver = controller.foxDriver

		for world, tab in tabs.items():
			print 'Going to another world!', world
			driver.switch_to_window(tab)
			controller.current_world = world
			controller.update_vars()
			game_state = controller.game.check_game_open()
			if game_state == False:
				username = controller.account_status['Username'].replace('\t', '')
				password = str(controller.account_status['Password']).strip()
				controller.cmd.log_in(username, password)
			controller.start_schedule()







