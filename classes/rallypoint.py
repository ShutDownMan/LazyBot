# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import collections

from css_paths import CSS_Paths as paths
from relative_paths import Relative_Paths as relative

units_quant_inputs = {
		'Spearman':		relative.RallyPoint_CreateSpearman,
		'Swordsman':	relative.RallyPoint_CreateSwordsman,
		'Viking':		relative.RallyPoint_CreateViking,
		'Archer':		relative.RallyPoint_CreateArcher,
		'Light Cv':		relative.RallyPoint_CreateLightCv,
		'Mnt Archer':	relative.RallyPoint_CreateMntArcher,
		'Heavy Cv':		relative.RallyPoint_CreateHeavyCv,
		'Berseker':		relative.RallyPoint_CreateBerseker
	}



class RallyPoint():

	units_predefs_hotkeys = {
		'Spearman':		1,
		'Swordsman':	2,
		'Viking':		3,
		'Archer':		4,
		'Light Cv':		5,
		'Mnt Archer':	6,
		'Heavy Cv':		7,
		'Berseker':		8
	}

	Master = None

	def __init__(self, master):
		self.Master = master
		print 'RallyPoint module loaded!\n' + str(master)

	def predefiniton_setup(self):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		village_status = self.Master.world_status

		if village_status == {}:
			print 'Invalid Village!'
			return

		undone_predefinitions = []

		# Adds all predefs to list
		for k,v in village_status.items():
			print k
			if k == 'Predefinitions':
				for unit, status in village_status[k].items():
					if 'None' in status:
						undone_predefinitions.append(unit)
				break

		if undone_predefinitions > 0:

			self.Master.game.select_game()

			print undone_predefinitions, '\n-------------'
			undone_predefinitions = self.check_global_predefs(undone_predefinitions)
			print undone_predefinitions

			self.create_predefinitions(undone_predefinitions)

		self.Master.ufile.update_village_status('PredefinitionsSetup', 'True', account, world, village)


	def check_global_predefs(self, undone_predefinitions=None):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'R')

		# Get to predefs menu
		rally_menu = self.Master.page.FindElem(paths.RallyPoint_Menu)

		if rally_menu == None:
			print 'Error on rally_menu when creating predefinition!'
			return

		global_predef_btn = rally_menu.find_element_by_xpath(relative.RallyPoint_ShowGlobal)
		self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', global_predef_btn)
		global_predef_btn.click()

		global_predefs = self.Master.page.FindElem(paths.RallyPoint_GlobalPredefs)

		if global_predefs == None:
			print 'Error on global_predefs when creating predefinition!'
			return

		defaults_list = []
		for unit, v in units_quant_inputs.items():
			defaults_list.append('[' + unit + ' Farming' + ']')
			undone_predefinitions.append(unit)

		# Runs through predefs and toggles the (disabled) default ones
		try:
			for i in range(50):
				current_predef = global_predefs.find_element_by_xpath(relative.RallyPoint_GlobalPredefName.replace('index', str(i+1)))

				if current_predef == None:
					print 'End of predef liste!'
					break

				toggle_btn = global_predefs.find_element_by_xpath(relative.RallyPoint_GlobalPredefToggle.replace('index', str(i+1)))

				current_predef_text = current_predef.text

				if current_predef_text in defaults_list:
					if 'switch-off' in self.Master.page.AttributeValue(toggle_btn, 'class'):
						print 'I told you not to touch the default predefs!'
						toggle_btn.click()
						undone_predefinitions.remove(unit)
						continue
					for unit in undone_predefinitions:
						if unit in current_predef_text:
							undone_predefinitions.remove(unit)
							continue

		except:
			print 'End of predef list!'
			pass

		self.Master.game.close_popup_menu(canvas)

		return undone_predefinitions

	def create_predefinitions(self, undone_predefinitions=None):
		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'R')

		rally_menu = self.Master.page.FindElem(paths.RallyPoint_Menu)

		if rally_menu == None:
			print 'Error on rally_menu when creating predefinition!'
			return

		units_ideal_division = self.calc_ideal_predef_division(self.current_unit_quant())


		for unit in undone_predefinitions:
			current_unit_ideal_quant = units_ideal_division[unit] if units_ideal_division[unit] > 10 else 20
			self.create_predef(unit, rally_menu, current_unit_ideal_quant)

			self.Master.ufile.update_village_status(unit, str(current_unit_ideal_quant), account, world, village, 'Predefinitions')

		self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', rally_menu)


	def create_predef(self, unit, rally_menu=None, ideal_unit_quant=30):

		if rally_menu != None:
			create_predef_btn = rally_menu.find_element_by_xpath(relative.RallyPoint_CreatePredef)
			self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', create_predef_btn)
			create_predef_btn.click()

			name_menu = self.Master.page.FindElem(paths.RallyPoint_NameMenu)

			if name_menu == None:
				print 'Error on name_menu when creating predefinition!'
				return
			name_input = name_menu.find_element_by_xpath(relative.RallyPoint_NameInput)
			name_ok = name_menu.find_element_by_xpath(relative.RallyPoint_NameOK)

			self.Master.page.Type(name_input, ('[' + unit + ' Farming' + ']'))
			name_ok.click()

			flag_menu = self.Master.page.FindElem(paths.RallyPoint_FlagCreating)

			if flag_menu == None:
				print 'Error on flag_menu when creating predefinition!'
				return

			self.setup_flags((1,1,13), flag_menu)

			create_menu = self.Master.page.FindElem(paths.RallyPoint_CreateMenu)

			if create_menu == None:
				print 'Error on create_menu when creating predefinition!'
				return

			closest_common = create_menu.find_element_by_xpath(relative.RallyPoint_ClosestCommon)

			units_inputs = closest_common.find_element_by_xpath(units_quant_inputs[unit])
			self.Master.page.Type(units_inputs, str(ideal_unit_quant))

			predef_hotkey = str(self.units_predefs_hotkeys[unit])

			set_hotkey = create_menu.find_element_by_xpath(relative.RallyPoint_SetHotkey.replace('index', predef_hotkey))
			self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', set_hotkey)
			set_hotkey.click()

			self.Master.game.wait(1)

			setto_attack = create_menu.find_element_by_xpath(relative.RallyPoint_SetToAttack.replace('index', predef_hotkey))
			setto_attack.click()

			self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', rally_menu)

			save_btn = create_menu.find_element_by_xpath(relative.RallyPoint_CreateSaveBtn)
			save_btn.click()



	def setup_flags(self, flag_order=(1,1,1), flag_menu=None):

		if flag_menu != None:
			flag_common = flag_menu.find_element_by_xpath(relative.RallyPoint_FlagCommon)
			for i in range(1,4):
				flag_path = (relative.RallyPoint_Buttons.replace('index', str(i)))
				''' Determines shortest path to desired flag '''
				flag = flag_order[i-1]
				flag = flag = flag-1 if flag < 16-flag else -(16-flag)-1

				if flag != 0:
					if flag > 0:
						up_btn = flag_common.find_element_by_xpath(flag_path.replace('jndex', '1'))
						# press up flag times
						for a in range(flag+1):
							up_btn.click()
							self.Master.game.wait(.1)
					else:
						down_btn = flag_common.find_element_by_xpath(flag_path.replace('jndex', '2'))
						# press down abs(flag) times
						for a in range(abs(flag)):
							down_btn.click()
							self.Master.game.wait(.1)

				flag_ok = flag_menu.find_element_by_xpath(relative.RallyPoint_OKButton)

				if flag_ok == None:
					print 'Error on flag_ok when creating predefinition!'
					return

			flag_ok.click()


	def modify_predefinition(self, unit_to_modify,  new_quant=None, new_flag=None, new_name=None):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'R')

		account = self.Master.current_account
		world = self.Master.current_world
		village = self.Master.current_village

		rally_menu = self.Master.page.FindElem(paths.RallyPoint_Menu)

		if rally_menu == None:
			print 'Error on rally_menu when creating predefinition!'
			return

		predef_to_modify = None

		try:
			i = 1
			while True:
				current_predef = rally_menu.find_element_by_xpath(relative.RallyPoint_Predefs.replace('index', str(i)))

				current_predef_text = current_predef.find_element_by_xpath(relative.RallyPoint_PredefName).text


				if '[' + unit_to_modify + ' Farming' + ']' == current_predef_text:
					predef_to_modify = current_predef
					break

				i += 1
				
		except:
			print 'End of predef list!'
			pass

		if predef_to_modify != None:
			if new_quant != None:
				self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', current_predef)
				
				modify_btn = predef_to_modify.find_element_by_xpath(relative.RallyPoint_EditPredef)
				modify_btn.click()

				# scroll up
				self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', rally_menu)

				create_menu = self.Master.page.FindElem(paths.RallyPoint_CreateMenu)

				if create_menu == None:
					print 'Error on create_menu when creating predefinition!'
					return

				closest_common = create_menu.find_element_by_xpath(relative.RallyPoint_ClosestCommon)

				unit_input = closest_common.find_element_by_xpath(units_quant_inputs[unit_to_modify])

				unit_input.clear()
				self.Master.page.Type(unit_input, str(new_quant))

				save_btn = create_menu.find_element_by_xpath(relative.RallyPoint_CreateSaveBtn)
				save_btn.click()

				self.Master.ufile.update_village_status(unit_to_modify, new_quant, account, world, village, "Predefinitions")

				print 'Modifying of predef '+unit_to_modify+' to new value '+new_quant+' was successfull!'
				pass
		pass


	def calc_ideal_predef_division(self, units_list={'Unit':0}):
		units_cc = collections.OrderedDict()
		totalSumCC = 0

		units_stats = self.Master.Units_Stats

		units_carrying_capacity = self.Master.Units_Stats

		for unit, quant in units_list.items():
			carry_capacity = int(units_carrying_capacity[unit]['Carrying Capacity'])
			totalSumCC += carry_capacity*quant
			units_cc.update({unit:carry_capacity})

	#	print 'Total carry capacity: ' + str(totalSumCC)+'\n----------'

		CCRationed = totalSumCC/float(50)
	#	print 'Ideal division per farm troop:\n' + str(CCRationed)+'\n----------'

		for k, v in units_cc.items():
			if v > 0:
				quant = round(CCRationed/v)
	#			print k+'s Farm:\n'	+ str(quant)+'\n----------'

		village_status = self.Master.world_status
		current_log = None

		for status, value in village_status.items():
			if 'Ideal troop division' in status:
				current_log = status

		return units_cc


	def current_unit_quant(self):
		unit_bar = self.Master.page.get_elem(paths.UnitQuant_UnitBar)
		units_stats = self.Master.Units_Stats
		unit_bar_parent = unit_bar.find_element_by_xpath('./..')

		if 'expanded' not in self.Master.page.AttributeValue(unit_bar_parent, 'class'):
			unit_bar_btn = unit_bar.find_element_by_xpath(relative.UnitQuant_ToggleUnit)
			unit_bar_btn.click()
			self.Master.game.wait(1)

		unit_quantity = {}

		for unit in units_stats:
			bar_id = units_stats[unit]['Unit Bar ID']
			unit_quant = unit_bar.find_element_by_xpath(relative.UnitQuant_UnitList.replace('index', str(bar_id))).text

			unit_quantity.update({unit:int(unit_quant)})

		return unit_quantity


	def total_unit_quant(self):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'U')

		unit_menu = self.Master.page.FindElem(paths.UnitQuant_UnitMenu)

		if unit_menu == None:
			print 'Error on unit_menu when creating predefinition!'
			return

		units_stats = self.Master.Units_Stats

		unit_quantity = {}

		for unit in units_stats:
			bar_id = units_stats[unit]['Unit Bar ID']
			unit_quant = unit_menu.find_element_by_xpath(relative.UnitQuant_UnitHorizontal.replace('index', str(hbar_id))).text

			unit_quantity[unit] = int(unit_quant)

		self.Master.game.select_game(unit_menu)

		return unit_quantity


# bot.game.calc_ideal_predef_division(bot.game.current_unit_quant())

# Must remove
	def wait(self, how_much):
		time.sleep(how_much)
	def select_game(self, canvas=None):
		if canvas == None:
			canvas = self.Master.page.get_elem(paths.Map_Canvas)
		canvas.click()
		self.Master.page.sendKeys(canvas, Keys.ESCAPE)

