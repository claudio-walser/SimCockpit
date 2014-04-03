#!/usr/bin/python
import time
from lib.Stepper import Motor

motor = Motor()
motor.initializePins()

motor.moveTo(20, False, 0.25)
motor.moveTo(40, False, 0.25)
motor.moveTo(60, False, 0.25)
motor.moveTo(80, False, 0.25)
motor.moveTo(100, False, 0.25)
motor.moveTo(120, False, 0.25)
motor.moveTo(140, False, 0.25)
motor.moveTo(160, False, 0.25)
motor.moveTo(180, False, 0.25)

motor.moveTo(160, False, 0.25)
motor.moveTo(140, False, 0.25)
motor.moveTo(120, False, 0.5)
motor.moveTo(100, False, 0.5)
motor.moveTo(80, False, 0.5)
motor.moveTo(60, False, 0.25)
motor.moveTo(40, False, 0.25)
motor.moveTo(20, False, 0.25)
motor.moveTo(0, False, 0.25)

motor.moveTo(-20, False, 0.25)
motor.moveTo(-40, False, 0.25)
motor.moveTo(-60, False, 0.25)
motor.moveTo(-80, False, 0.25)
motor.moveTo(-100, False, 0.25)
motor.moveTo(-120, False, 0.25)
motor.moveTo(-140, False, 0.25)
motor.moveTo(-160, False, 0.25)
motor.moveTo(-180, False, 0.25)
motor.moveTo(-200, False, 0.25)
motor.moveTo(-220, False, 0.25)
motor.moveTo(-240, False, 0.25)
motor.moveTo(-260, False, 0.25)
motor.moveTo(-280, False, 0.25)
motor.moveTo(-300, False, 0.25)
motor.moveTo(-320, False, 0.6)
motor.moveTo(-340, False, 0.6)
motor.moveTo(-360, False, 0.6)
motor.moveTo(-380, False, 0.25)

motor.moveTo(0, 120)


#motor.move(512, 'clockwise', 100)
#for i in range(18):
#	i += 1
#	motor.moveTo(i * 20, False, 0.25)
	

motor.cleanup()
#motor.move(28)
#for i in range(360):
#	motor.moveTo(i, 'clockwise', 100)
#	time.sleep(0.0001)
#time.sleep(1)
#motor.moveTo(90, 'clockwise', 'slow')