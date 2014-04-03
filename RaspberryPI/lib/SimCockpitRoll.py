#!/usr/bin/env python
from SimCockpit import SimCockpit
from lib.Stepper import Motor

# SimCockpit pitch processor
class SimCockpitRoll(SimCockpit):

	motor = False

	def init(self):
		self.motor = Motor()
		self.motor.initializePins()

	def process(self, data):
		# overwrite this function
		#self.motor.moveTo(float(data), 'clockwise', 'slow')
		self.logging.debug(data)
		self.logging.debug(self.motor)
		try:
			self.motor.moveTo(float(data), False, 0.25)
			#self.motor.moveTo(float(data), 'clockwise', 'slow')
		except Exception as (errno, strerror):
			self.logging.debug("I/O error(%s): %s" % (errno, strerror))
		
		