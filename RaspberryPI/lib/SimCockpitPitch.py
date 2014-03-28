#!/usr/bin/env python
from SimCockpit import SimCockpit

# SimCockpit pitch processor
class SimCockpitPitch(SimCockpit):

	def process(self, data):
		# overwrite this function
		self.logging.debug(data)