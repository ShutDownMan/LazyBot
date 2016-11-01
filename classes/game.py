# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from selenium.webdriver.common.keys import Keys

from css_paths import CSS_Paths as paths
from relative_paths import Relative_Paths as relative

class Game():

	Master = None

	def __init__(self, master):
		self.Master = master
		print "Game module loaded!\n" + str(master)


	def wait(self, how_much):
		time.sleep(how_much)


	def select_game(self, canvas=None):
		if canvas == None:
			canvas = self.Master.page.FindElem(paths.Map_Canvas, 20)
		canvas.click()
		self.Master.page.sendKeys(canvas, Keys.ESCAPE)
		

	def close_popup_menu(self, canvas=None):
		if canvas == None:
			canvas = self.Master.page.get_elem(paths.Map_Canvas)
		canvas.click()

	def check_game_open(self):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)

		if canvas != None:
			print 'Already logged in!'
			return True

		return False

	def current_unit_quant(self):
		unit_bar = self.Master.page.get_elem(paths.UnitQuant_UnitBar)

		unit_bar_parent = unit_bar.find_element_by_xpath('./..')

		if "expanded" not in self.Master.page.AttributeValue(unit_bar_parent, "class"):
			unit_bar_btn = unit_bar.find_element_by_xpath(relative.UnitQuant_ToggleUnit)
			unit_bar_btn.click()
			self.Master.game.wait(1)

		unit_quant = [1,2,3,4,5,6,7,10]

		for i in range(8):
			unit_quant = unit_bar.find_element_by_xpath(relative.UnitQuant_UnitList.replace('index', str(unit_quant[i]))).text

			unit_quant[i] = int(unit_quant)

		return unit_quant


	def total_unit_quant(self):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.Type(canvas, "U")

		unit_menu = self.Master.page.FindElem(paths.UnitQuant_UnitMenu)

		if unit_menu == None:
			print "Error on unit_menu when creating predefinition!"
			return

		unit_quant = [1,2,3,4,5,6,7,10]
		
		for i in range(8):
			unit_quant = unit_menu.find_element_by_xpath(relative.UnitQuant_UnitHorizontal.replace('index', str(unit_quant[i]))).text

			unit_quant[i] = int(unit_quant)

		self.Master.game.select_game(unit_menu)

		return unit_quant

	def current_time(self):
		return time.time()

	def calculate_dist(self, origin=(0,0),dest=(0,0)):
		z1 = origin[0] + 0.5 if self.isodd(origin[1]) else origin[0] - 0.5
		z2 = dest[0] + 0.5 if self.isodd(dest[1]) else dest[0] - 0.5
		d1 = sqrt((z1 - z2)**2 + 0.75 * (origin[1] - dest[1])**2)
		d2 = sqrt((origin[0] - dest[0])**2 + 0.75 * (origin[1] - dest[1])**2)
		d = (d1 + d2) / 2
		return d

	def isodd(self, number=0):
		if number%2==0:
			return False
		else:
			return True


	def dist_in_time(dist, slowest_unit, barbarian=False):
		unit_stats = ''
		EnPointLine = ''
		VelocityIncrease = 0

		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		unit_velocity = self.Master.Units_Stats[slowest_unit]['Velocity']

		unit_velocity = self.to_seconds(unit_velocity)

		timeDist = dist*unit_velocity

		if barbarian == True:

			village_status = self.Master.world_status
			raidPathlvl = int(village_status[account][world]['Tribe']['Raiding Path'])
			rallypoint_lvl = int(village_status[account][world][village]['Rally Point'])

			VelocityIncrease += rallypoint_lvl*50

			newTime = timeDist/(1 + (VelocityIncrease/100.0))/1+(raidPathlvl/10.0)

			return newTime

		else:

			return timeDist


	def to_seconds(self, s):
		hr, min, sec = [float(x) for x in s.split(':')]
		return hr*3600 + min*60 + sec
