# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from css_paths import CSS_Paths as paths
from relative_paths import Relative_Paths as relative

class Resource_Gather():

	Master = None
	
	def __init__(self, master):
		self.Master = master

	def gather_resources(self):
		dropdown_menu = self.Master.page.FindElem(paths.VillageDropdown_Menu)

		world_status = self.Master.world_status
		gather_village = world_status['Resource Deposit']

		if dropdown_menu == None:
			print "Page don't seem to be loaded properly!"
			return

		dropdown_menu_btn = dropdown_menu.find_element_by_xpath(relative.VillageDropdown_Button)
		dropdown_menu_btn.click()

		self.Master.game.wait(3)

		dropdown_list = dropdown_menu.find_element_by_xpath(relative.VillageDropdown_List)

		if dropdown_list == None:
			print "Page don't seem to be loaded properly!"
			return

		dropdown_villages = dropdown_list.find_elements_by_xpath('./tr')

		resource_deposit = None
		for i in range(1, len(dropdown_villages)):
			village_path = relative.VillageDropdown_Village.replace('index', str(i))
			village = dropdown_list.find_element_by_xpath(village_path.replace('jndex', '2'))

			if 'arrow-up' in self.Master.page.AttributeValue(village, 'class'):
				resource_deposit = village
				village.click()
				continue

			village = dropdown_list.find_element_by_xpath(village_path.replace('jndex', '1'))

			if gather_village == village.text.replace(' ', ''):
				village.click()
				break

		dropdown_menu_btn.click()

		wrapper = self.Master.page.FindElem(paths.ResDeposity_Wrapper)

		if wrapper == None:
			print "Page don't seem to be loaded properly!"
			return

		job_done = wrapper.find_element_by_xpath(relative.ResDeposit_JobDone)

		job_done.click()

		new_job = wrapper.find_element_by_xpath(relative.ResDeposit_NewJob)

		new_job.click()

		self.Master.game.select_game()
