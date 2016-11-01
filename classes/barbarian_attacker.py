# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium.webdriver.common.keys import Keys

from css_paths import CSS_Paths as paths
from relative_paths import Relative_Paths as relative

class BarbarianAttacker():

	Master = None

	def __init__(self, master):
		self.Master = master
		print "Barbarian_Attacker module loaded!\n" + str(master)


	def attack_nearest_barbarians(self):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village
	# update attacks log
	#	troops_to_send = get_predefs_available()
	#	self.Master.page.sendKeys(Keys.ESCAPE)

	#	if troops_to_send == '':
	#		print "No troops no farming =/"
	#		return

		closest_barbarians = self.Master.ufile.get_closest_barbarians()
	#	print closest_barbarians

		# get all attacks list
		attacks_log = self.Master.ufile.get_attacks_log(self.Master.current_village)

		# loop through barbarians
		for barbarian in closest_barbarians:
			if barbarian in attacks_log:
				if attacks_log['Attacks occouring'] < 50:

					barb_log = attacks_log[barbarian]
					current_time = self.Master.game.current_time()

					if current_time > float(barb_log['Wait Until']):
						# attack village (barbarian)
						barbarian_coord = barbarian.split('|')
						self.attack_village(int(barbarian_coord[0]), int(barbarian_coord[1]), "Spearman")
						# log attack
						
						self.Master.ufile.update_attack_status(barbarian, current_time, village)


	def attack_village(self, village_to_attack, unit_to_attack):
		self.globe_map.SearchCoords((village_to_attack))

		menu_highlight = self.Master.page.FindElem(paths.Misc_MenuHighlight)

		if menu_highlight == None:
			print 'Error on menu_highlight when attacking village!'
			return

		self.Master.page.sendKeys(self.Master.rallypoint.units_predefs_hotkeys[unit_to_attack])

		# hope it worked


	def check_troops(self):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(Keys.ESCAPE)
		self.Master.page.Type(canvas, "R")


	def get_current_village(self):
		pass

