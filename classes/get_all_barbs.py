# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from StringIO import StringIO
from PIL import Image


class UpdateBarbarianList():

	Master = None

	def __init__(self, master):
		self.Master = master
		print "UpdateBarbarianList module loaded!\n" + str(master)


	def get_barbs(self):
		world = self.Master.current_world
		barbarians_map = self.Master.BarbariansMap[world].replace('"', '')
		response = requests.get(barbarians_map)
		img = Image.open(StringIO(response.content))

		barb_list = []

		xCord = 66
		yCord = 65

		for y in range(270):
			yCord += 3
			for x in range(270):
				xCord += 3
				if img.getpixel((xCord, yCord)) == (102, 102, 102):
					print 'Barbarian at ' + str((xCord, yCord))
					x_Coord = xCord/3+329
					y_Coord = yCord/3+330
					print 'in other words, at ' + str(x_Coord) + '|' + str(y_Coord) + '\n---------------------'

					barb_list.append((x_Coord, y_Coord))
			xCord = 66

		return barb_list

	# 000 000 = 397|397

	# 420 480 = 481|493

	# 450 480 = 487|493

	# 684 408 = 557|465

	# 481 411 = 556|466

	# 30 = 6
	# 5p por 1xy