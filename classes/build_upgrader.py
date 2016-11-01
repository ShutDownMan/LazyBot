# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from selenium.webdriver.common.keys import Keys

from css_paths import CSS_Paths as paths
from relative_paths import Relative_Paths as relative

Buildings =	{"HEAD QUARTER":	relative.Build_HeadQuarter,
			"TIMBER CAMP":		relative.Build_TimberCamp,
			"CLAY PIT":			relative.Build_ClayPit,
			"IRON MINE":		relative.Build_IronMine,
			"FARM":				relative.Build_Farm,
			"WAREHOUSE":		relative.Build_Warehouse,
			"RALLY POINT":		relative.Build_RallyPoint,
			"BARRACKS":			relative.Build_Barracks,
		#	"":paths.Build_
		#	"":paths.Build_
		#	"":paths.Build_
		#	"":paths.Build_
		#	"":paths.Build_
		#	"":paths.Build_
		#	"":paths.Build_
			"":					paths.Map_Canvas}

class Build_Upgrader():
	Master = None

	def __init__(self, master):
		self.Master = master
		print "Build Upgrader loaded!\n" + str(master)

	def check_build_schedule(self):
		build_schedule = self.get_build_schedule()

		for build in build_schedule:
			self.check_green_mark()
			success = self.upgrade_building(build)
			if success == False:
				break


	def check_green_mark(self):
		elem = self.Master.page.get_elem(paths.Build_Finish_Build)
		if elem != None:
			elem.click()
			print "Green Mark!"
		else:
			print "No Green Mark"

	def upgrade_building(self, building):
		canvas = self.Master.page.get_elem(paths.Map_Canvas)
		self.Master.game.select_game(canvas)
		self.Master.page.Type(canvas, "H")

		success = False

		boxPaper = self.Master.page.FindElem(paths.Build_BoxPaper)
		if boxPaper != None:
			print "Building Menu loaded!"


		buildingBtn = boxPaper.find_element_by_xpath(Buildings[building.upper()])
		classAttr = self.Master.page.AttributeValue(buildingBtn, "class")
		btn_orange = len(classAttr)
		btn_grey = 0

		try:
			btn_orange = classAttr.index("btn-orange")
			btn_grey = classAttr.index("btn-grey")
		except:
			print "Error on upgrade buildings"

		self.Master.foxDriver.execute_script("return arguments[0].scrollIntoView();", buildingBtn)

		if buildingBtn != None and btn_orange > btn_grey:
			buildingBtn.click()
			print "Successfully upgraded building: " + building
			success = True
		else:
			print "Couldn't upgrade building: " + building
			success = False

		self.Master.foxDriver.execute_script('return arguments[0].scrollIntoView();', boxPaper)

		self.Master.game.select_game()

		return success


	def get_build_schedule(self):
		village_status = self.Master.village_status
		print village_status
		build_schedule = village_status['Build Schedule']
		return build_schedule

