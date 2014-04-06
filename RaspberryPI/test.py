#!/usr/bin/python
import time
from lib.Stepper import Motor

motor = Motor()
motor.initializePins()

motor.moveTo(0.00, False, 0.3)
motor.moveTo('0.13-0.48-1.40', False, 0.3)





motor.moveTo(0.13, False, 0.3)
motor.moveTo(-0.48, False, 0.3)
motor.moveTo(-1.40, False, 0.3)
motor.moveTo(-1.79, False, 0.3)
motor.moveTo(-1.80, False, 0.3)
motor.moveTo(-1.87, False, 0.3)
motor.moveTo(-1.96, False, 0.3)
motor.moveTo(-2.08, False, 0.3)
motor.moveTo(-2.80, False, 0.3)
motor.moveTo(-5.69, False, 0.3)
motor.moveTo(-11.20, False, 0.3)
motor.moveTo(-18.74, False, 0.3)
motor.moveTo(-28.00, False, 0.3)
motor.moveTo(-38.04, False, 0.5)
motor.moveTo(-47.87, False, 0.5)
motor.moveTo(-57.25, False, 0.5)
motor.moveTo(-66.24, False, 0.3)
motor.moveTo(-74.98, False, 0.3)
motor.moveTo(-83.62, False, 0.3)
motor.moveTo(-92.27, False, 0.3)
motor.moveTo(-101.13, False, 0.3)
motor.moveTo(-110.37, False, 0.3)
motor.moveTo(-120.07, False, 0.3)
motor.moveTo(-130.25, False, 0.3)
motor.moveTo(-140.90, False, 0.3)
motor.moveTo(-152.01, False, 0.3)
motor.moveTo(-163.67, False, 0.3)
motor.moveTo(-176.05, False, 0.3)
# fix this change at 180 degree, either in game export or in stepper moveTo
motor.moveTo(170.74, False, 0.3)
motor.moveTo(156.84, False, 0.3)
motor.moveTo(142.69, False, 0.3)
motor.moveTo(128.93, False, 0.3)
motor.moveTo(115.94, False, 0.3)
motor.moveTo(103.54, False, 0.3)

motor.moveTo(90.69, False, 0.3)

motor.moveTo(103.54, False, 0.3)
motor.moveTo(115.94, False, 0.3)
motor.moveTo(128.93, False, 0.3)
motor.moveTo(142.69, False, 0.3)
motor.moveTo(156.84, False, 0.3)
motor.moveTo(170.74, False, 0.3)
print 'seems good so far'
# problem here
motor.moveTo(-176.05, False, 0.3)
motor.moveTo(-163.67, False, 0.3)
motor.moveTo(-152.01, False, 0.3)
motor.moveTo(-140.90, False, 0.3)
motor.moveTo(-130.25, False, 0.3)
motor.moveTo(-120.07, False, 0.3)
# set back to zero
#motor.moveTo(0, 120)


#motor.move(512, 'clockwise', 100)
#for i in range(18):
#	i += 1
#	motor.moveTo(i * 20, False, 0.3)
	


#motor.move(28)
#for i in range(360):
#	motor.moveTo(i, 'clockwise', 100)
#	time.sleep(0.0001)
#time.sleep(1)
#motor.moveTo(90, 'clockwise', 'slow')

motor.cleanup()
