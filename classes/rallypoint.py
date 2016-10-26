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

	Master = None

	def __init__(self, master):
		self.Master = master
		print 'RallyPoint module loaded!\n' + str(master)

	def predefiniton_setup(self):
		village_status = self.Master.ufile.get_village_status('[0x00 - Village]')
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

			self.check_global_predefs(undone_predefinitions)

			self.create_predefinitions(undone_predefinitions)

		self.Master.ufile.update_village_status('PredefinitionsSetup', 'True', '[0x00 - Village]')


	def check_global_predefs(self, undone_predefinitions=None):

		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'R')

		# Get to predefs menu
		rally_menu = self.Master.page.FindElem(paths.RallyPoint_Menu)

		if rally_menu == None:
			print 'Error on rally_menu when creating predefinition!'
			return


		global_predef_btn = rally_menu.find_element_by_xpath(relative.RallyPoint_ShowGlobal)
		global_predef_btn.click()


		global_predefs = self.Master.page.FindElem(paths.RallyPoint_GlobalPredefs)


		if global_predefs == None:
			print 'Error on global_predefs when creating predefinition!'
			return

		# Runs through predefs and toggles the (disabled) default ones
		try:
			for i in range(50):
				print i+1
				current_predef = global_predefs.find_element_by_xpath(relative.RallyPoint_GlobalPredefName.replace('index', str(i+1)))

				if current_predef == None:
					print 'End of predef liste!'
					break

				toggle_btn = global_predefs.find_element_by_xpath(relative.RallyPoint_GlobalPredefToggle.replace('index', str(i+1)))

				for unit in undone_predefinitions:
					if '[' + unit + ' Farming' + ']' == current_predef.text:
						if 'switch-off' in self.Master.page.AttributeValue(toggle_btn, 'class'):
							self.Master.ufile.update_village_status(unit, '0', '[0x00 - Village]', 'Predefinitions')
							toggle_btn.click()
						break

				for unit, v in units_quant_inputs.items():
					if '[' + unit + ' Farming' + ']' == current_predef.text:
						if 'switch-off' in self.Master.page.AttributeValue(toggle_btn, 'class'):
							print 'I told you not to touch the default predefs!'
							toggle_btn.click()

				self.Master.game.wait(.3)

		except:
			print 'End of predef list!'
			pass

		self.Master.game.select_game()


	def create_predefinitions(self, undone_predefinitions=None):
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

			self.Master.ufile.update_village_status(unit, str(current_unit_ideal_quant), '[0x00 - Village]', 'Predefinitions')


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

			save_btn = create_menu.find_element_by_xpath(relative.RallyPoint_CreateSaveBtn)

			save_btn.click()



	def setup_flags(self, flag_order=(1,1,13), flag_menu=None):

		if flag_menu != None:
			flag_common = flag_menu.find_element_by_xpath(relative.RallyPoint_FlagCommon)
			for i in range(1,4):
				flag_path = (relative.RallyPoint_Buttons.replace('index', str(i)))
				print flag_path
				''' Determines shortest path to desired flag '''
				flag = flag_order[i-1]
				flag = flag = flag-1 if flag < 16-flag else -(16-flag)-1
				print flag

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

		rally_menu = self.Master.page.FindElem(paths.RallyPoint_Menu)

		if rally_menu == None:
			print 'Error on rally_menu when creating predefinition!'
			return

		predefs = rally_menu.find_element_by_xpath(relative.RallyPoint_Predefs)

		predef_to_modify = None

		try:
			i = 1
			while True:
				current_predef = predefs.find_element_by_xpath(relative.RallyPoint_PredefName.replace('index', str(i)))

				if unit_to_modify in current_predef.text:
					predef_to_modify = current_predef

			i += 1
		except:
			print 'End of predef list!'
			pass

		if current_predef != None:
			if new_quant != None:
				modify_btn = current_predef.find_element_by_xpath(relative.RallyPoint_EditPredef)
				modify_btn.click()

				create_menu = self.Master.page.FindElem(paths.RallyPoint_CreateMenu)

				if create_menu == None:
					print 'Error on create_menu when creating predefinition!'
					return

				closest_common = create_menu.find_element_by_xpath(relative.RallyPoint_ClosestCommon)

				units_inputs = closest_common.find_element_by_xpath(units_quant_inputs[unit])

				self.Master.page.Type(units_inputs, str(new_quant))

				pass

		pass

	def calc_ideal_predef_division(self, troops, village=''):
		troops_cc = collections.OrderedDict()
		totalSumCC = 0

		troops_carrying_capacity = self.Master.ufile.get_config('Troops Carrying Capacity')
		i = 0
		for line in troops_carrying_capacity:
			m_stat = line.replace('\t','')
			m_stat = m_stat.strip()
			splited = m_stat.split('>')
			totalSumCC += int(splited[1])*troops[i]
			troops_cc.update({str(splited[0]):int(splited[1])})
			i += 1

	#	print 'Total carry capacity: ' + str(totalSumCC)+'\n----------'

		CCRationed = totalSumCC/float(50)
	#	print 'Ideal division per farm troop:\n' + str(CCRationed)+'\n----------'

		for k, v in troops_cc.items():
			if v > 0:
				quant = round(CCRationed/v)
	#			print k+'s Farm:\n'	+ str(quant)+'\n----------'

		if village != '':
			village_status = self.Master.ufile.get_village_status('[0x00 - Village]')
			current_log = None

			for status, value in village_status.items():
				if 'Ideal troop division' in status:
					current_log = status

		return troops_cc


	def current_unit_quant(self):
		unit_bar = self.Master.page.get_elem(paths.UnitQuant_UnitBar)

		unit_bar_parent = unit_bar.find_element_by_xpath('./..')

		if 'expanded' not in self.Master.page.AttributeValue(unit_bar_parent, 'class'):
			unit_bar_btn = unit_bar.find_element_by_xpath(relative.UnitQuant_ToggleUnit)
			unit_bar_btn.click()
			self.Master.game.wait(1)

		unit_quantity = [1,2,3,4,5,6,7,10]

		for i in range(8):
			unit_quant = unit_bar.find_element_by_xpath(relative.UnitQuant_UnitList.replace('index', str(unit_quantity[i]))).text

			unit_quantity[i] = int(unit_quant)

		return unit_quantity


	def total_unit_quant(self):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.page.sendKeys(canvas, 'U')

		unit_menu = self.Master.page.FindElem(paths.UnitQuant_UnitMenu)

		if unit_menu == None:
			print 'Error on unit_menu when creating predefinition!'
			return

		unit_quantity = [1,2,3,4,5,6,7,10]
		
		for i in range(8):
			unit_quant = unit_menu.find_element_by_xpath(relative.UnitQuant_UnitHorizontal.replace('index', str(unit_quantity[i]))).text

			unit_quantity[i] = int(unit_quant)

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

