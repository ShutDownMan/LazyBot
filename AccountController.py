# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from WorldController import WorldController


class AccountController():

	windows = {}

	def __init__(self, startbrowser=True):
		if startbrowser:
			self.start_bot()
		

	def start_bot(self):
		self.open_account("LazyShut")

	def open_account(self, account):
		world_controller = WorldController(account)

		world_controller.account = account

		self.windows.update({account:world_controller})
