#!/usr/bin/env python
from SimCockpit import SimCockpit

# SimCockpit pitch processor
class SimCockpitRoll(SimCockpit):

	def process(self, data):
		# overwrite this function
		self.logging.debug(data)