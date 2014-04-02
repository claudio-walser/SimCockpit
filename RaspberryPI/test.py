#!/usr/bin/python
import time
from lib.Stepper import Motor

motor = Motor()
motor.initializePins()
#motor.move(28)
for i in range(360):
	motor.moveTo(i, 'clockwise', 'slow')
	time.sleep(0.0001)
#time.sleep(1)
#motor.moveTo(90, 'clockwise', 'slow')