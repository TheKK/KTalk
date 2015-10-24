# -*- coding: utf-8 -*-

import json
import os

STATES_FILE = './states'

# Define states entrys
STATES_LAST_UPDATE_TIME = "last_update_time"

class States(object):
	def __init__(self):
		self._states = {}

		# Check if STATE_FILE exist
		if not os.path.isfile(STATES_FILE):
			with open(STATES_FILE, 'a') as fp:
				fp.write('{}')

		with open(STATES_FILE, 'rb') as fp:
			self._states = json.loads(fp.read())
		print('hi')
	
	def __del__(self):
		with open(STATES_FILE, 'wb') as fp:
		    fp.write(json.dumps(self._states))
		print('bye')

	def getLastNewsUpdateTime(self):
		return self._state[STATES_LAST_UPDATE_TIME]

	def setLastNewsUpdateTime(self, time):
		self._states[STATES_LAST_UPDATE_TIME] = time
