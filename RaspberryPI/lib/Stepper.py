#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Stepper Motor Controller
class Motor():

	# used pins to control the motor
	# these are the exact GPIO numbers, corresponding to 11, 12, 13, 15 to raspberry pin numbers
	# http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/ (Revision 2)
	pins = [17, 18, 27, 22]

	# gear transmission ratio
	transmissionRatio = 1

	# current angle 
	currentAngle = 0

	# motor full step matrix
	fullStep = [
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]

	# steps for a full revolution
	stepsPerRevolution = 512

	# motor half step matrix
	halfStep = [
		[1, 0, 0, 0],
		[1, 1, 0, 0],
		[0, 1, 0, 0],
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 1, 1],
		[0, 0, 0, 1],
		[1, 0, 0, 1]
	]

	pinsInitialized = False

	logging = False

	def setLogging(self, logging):
		self.logging = logging

	def setPins(self, pin1, pin2, pin3, pin4):
		self.pins = [pin1, pin2, pin3, pin4]


	def initializePins(self):
		try:
			if self.pinsInitialized == True:
				return
			self.pinsInitialized = True
			GPIO.setmode(GPIO.BCM)
			for pin in self.pins:
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin, 0)
		except Exception as (errno, strerror):
			if self.logging != False:
				self.logging.debug("I/O error(%s): %s" % (errno, strerror))
			return

	def moveTo(self, angle, direction, speed):
		# make sure not bigger 360 and make 360 equals to zero
		while angle > 360:
			angle -= 360

		degreePerStep = float(360) / float(self.stepsPerRevolution)
		# make sure angle is in possible stepper range
		targetAngle = int(angle / degreePerStep) * degreePerStep

		if self.currentAngle < targetAngle:
			angleDifference = targetAngle - self.currentAngle
			direction = 'clockwise'
		else:
			angleDifference = self.currentAngle - targetAngle
			direction = 'anticlockwise'
		
		stepsToGo = angleDifference / degreePerStep

		self.move(stepsToGo, direction)

		#print stepsToGo
		#print targetAngle

		self.currentAngle = targetAngle
                


	def move(self, steps, direction):		
		speed = 'slow'
		#speed = 'fast'
		
		if speed == 'slow':
			stepMatrix = self.halfStep
		else:
			stepMatrix = self.fullStep

		if direction != 'clockwise':
			print 'doesent work yet'
			for key, steps in stepMatrix:
				stepMatrix[key] = reversed(steps)
			#stepMatrix = reversed(stepMatrix)

		# loop to set pins
		for i in range(int(steps)):
			for step in stepMatrix:
				for pin in range(len(self.pins)):
					print 'Set pin number GPIO%s to %s' % (self.pins[pin], step[pin])
					GPIO.output(self.pins[pin], step[pin])
				# play with the speed a little, dont go over 0.01
				time.sleep(0.0005)

		for pin in self.pins:
		#	print 'Set pin number GPIO%s to off' % pin
			GPIO.output(pin, 0)