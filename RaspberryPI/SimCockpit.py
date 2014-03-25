#!/usr/bin/python

from daemon import Daemon
import sys
import time
import logging
import socket

PIDFILE = '/var/run/simcockpit.pid'
LOGFILE = '/var/log/simcockpit.log'

HOST = '10.20.0.90'
PORT = 50007

PITCH_CLIENT = '10.20.0.90'
PITCH_PORT = 50008

ROLL_CLIENT = '10.20.0.92'
ROLL_PORT = 50008

# Configure logging
logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)

class SimCockpit(Daemon):

	socket = ''
	socketPitch = ''
	socketRoll = ''


	def initSocket(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketPitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketRoll = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# listen on main port for game input
		self.socket.bind((HOST, PORT))
		self.socket.listen(5)

		# connect pitch controller
		self.socketPitch.connect((PITCH_CLIENT, PITCH_PORT))
		self.socketRoll.connect((ROLL_CLIENT, ROLL_PORT))

	def closeSocket(self):
		if self.socket != '':
			self.socket.close()
		if self.socketPitch != '':
			self.socketPitch.close()
		if self.socketRoll != '':
			self.socketRoll.close()

	def receive(self):
		(connection, address) = self.socket.accept()
		data = True
		while data:
			data = connection.recv(4096)
			
			# extract pitch and roll and pass it to its engine controllers
			lines = data.split("\n")
			# not quite sure why, sometimes more lines are comming into this 4096 bytes, have to play with that
			for line in lines:
				if  line != '':
					logging.debug(line)
					values = line.split('|')
					for value in values:
					
						label_value = value.split(':')
						if len(label_value) == 2:
							logging.debug(label_value)
							logging.debug(len(label_value))
							label = label_value[0]
							value = label_value[1]
							if label == 'Roll':
								self.socketRoll.send(value)
							elif label == 'Pitch':
								self.socketPitch.send(value)

			

			
			#self.socketPitch.send(data)
			#self.socketRoll.send(data)
			# log
			#logging.debug(data)

	def run(self):
		self.initSocket()

		while True:
			#accept connections from outside
			self.receive()
		


if __name__ == "__main__":

	daemon = SimCockpit(PIDFILE)

	if len(sys.argv) == 2:

		if 'start' == sys.argv[1]:
			print "Starting ..."
			try:
				daemon.start()
			except:
				pass

		elif 'stop' == sys.argv[1]:
			print "Stopping ..."
			daemon.closeSocket()
			daemon.stop()

		elif 'restart' == sys.argv[1]:
			print "Restaring ..."
			daemon.restart()

		elif 'status' == sys.argv[1]:
			try:
				pf = file(PIDFILE,'r')
				pid = int(pf.read().strip())
				pf.close()
			except IOError:
				pid = None
			except SystemExit:
				pid = None

			if pid:
				print '%s is running as pid %s' % (sys.argv[0], pid)
			else:
				print '%s is not running.' % sys.argv[0]

		else:
			print "Unknown command"
			sys.exit(2)
			sys.exit(0)
	else:
		print "usage: %s start|stop|restart|status" % sys.argv[0]
		sys.exit(2)

