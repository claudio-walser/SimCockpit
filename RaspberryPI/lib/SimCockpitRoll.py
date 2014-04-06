#!/usr/bin/env python
from SimCockpit import SimCockpit
from lib.Stepper import Motor

# SimCockpit roll processor
class SimCockpitRoll(SimCockpit):

	motor = False

	def init(self, logging):
		super(SimCockpitRoll, self).init(logging)
		
		self.motor = Motor()
		self.motor.setLogging(self.logging)
		self.motor.initializePins()

	def process(self, data):
		# overwrite process function
		self.logging.debug(data)
		try:
			self.motor.moveTo(float(data), False, 0.3)
		except Exception as (errno, strerror):
			self.logging.debug("I/O error(%s): %s" % (errno, strerror))
		
		
