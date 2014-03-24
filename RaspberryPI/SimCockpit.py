#!/usr/bin/python

from daemon import Daemon
import sys
import time
import logging
import socket

HOST = '10.20.0.90'
PORT = 50007
PIDFILE = '/var/run/simcockpit.pid'
LOGFILE = '/var/log/simcockpit.log'


# Configure logging
logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)

class SimCockpit(Daemon):

	socket = ''

	def initSocket(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((HOST, PORT))
		self.socket.listen(5)

	def closeSocket(self):
		self.socket.close()


	def receive(self):
		(connection, address) = self.socket.accept()
		data = True
		while data:
			data = connection.recv(4096)
			# extract pitch and roll and pass it to its engine controllers
			logging.debug(data)

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

