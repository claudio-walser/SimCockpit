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

	# steps for a full revolution / just for half steps, full step is around 529??, dont get it yet
	stepsPerRevolution = 512

	# values from testing, table for speed value / seconds per full revolution (spr)
	# speed   |   spr   |   ratio
	# ---------------------------
	#   128   |  4.00   |    34.5
	#    70   |  6.15   |    13.0
	#    30   | 11.25   |     3.5
	#    20   | 14.70   |     2.0
	#    10   | 21.50   |     0.9
	#     0   | 42.00   |     0.2
	maxSpeed = 128

	# max degree the motor can do in a second, its actually 90, this is a little seurity gap
	maxDegreePerSecond = 80

	# motor half step matrix and the same for reverse
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

	halfStepReverse = [
		[0, 0, 0, 1],
		[0, 0, 1, 1],
		[0, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0],
		[1, 1, 0, 0],
		[1, 0, 0, 0],
		[1, 0, 0, 1]
	]

	pinsInitialized = False

	logging = False

	latency = 0.0

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

	def cleanup(self):
		GPIO.cleanup()
	
	def resetPins(self):
		for pin in self.pins:
			GPIO.output(pin, 0)

	def moveTo(self, angle, speed, interval = False):
		# make sure not bigger 360 and make 360 equals to zero
		while angle > 360:
			angle -= 360

		angle = angle / self.transmissionRatio

		degreePerStep = float(360) / float(self.stepsPerRevolution)
		# make sure angle is in possible stepper range
		targetAngle = int(angle / degreePerStep) * degreePerStep

		if self.currentAngle < targetAngle:
			angleDifference = targetAngle - self.currentAngle
			direction = 'clockwise'
		else:
			angleDifference = self.currentAngle - targetAngle
			direction = 'counter-clockwise'
		
		stepsToGo = angleDifference / degreePerStep

		if interval == False:
			timeSleep = False
		else:
			# check on max speed
			if (self.maxDegreePerSecond / (1 / interval) + 0.5) < angleDifference:
				
				if self.logging != False:
					self.logging.debug('Way too much boy, try next or as soon as you get close')
	
				return
	
			timeSleep = (interval - self.latency) / (stepsToGo * 10)

		self.move(stepsToGo, direction, speed, timeSleep)

		if targetAngle == 360 or targetAngle == -360:
			targetAngle = 0
		self.currentAngle = targetAngle


	def move(self, steps, direction, speed, timeSleep = False):		
		
		if timeSleep == False:
			# check speed
			if speed > self.maxSpeed:
				speed = self.maxSpeed
			elif speed <= 0:
				speed = 0
			speed += 10
			sleep_time = 0.1 / float(speed)
		else:
			sleep_time = timeSleep
		
		stepMatrix = self.halfStep
		
		if direction != 'clockwise':
			stepMatrix = self.halfStepReverse
			# does not work :(
			#for index, step in enumerate(stepMatrix):
			#	stepMatrix[index] = step
		

		# loop to set pins
		for i in range(int(steps)):
			for step in stepMatrix:
				for pin in range(len(self.pins)):
					#print 'Set pin number GPIO%s to %s' % (self.pins[pin], step[pin])
					GPIO.output(self.pins[pin], step[pin])
				# play with the speed a little, dont go over 0.01
				time.sleep(sleep_time)

		self.resetPins()