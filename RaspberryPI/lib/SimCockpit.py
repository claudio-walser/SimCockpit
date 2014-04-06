#!/usr/bin/env python
import sys
import socket
from Daemon import Daemon

# SimCockpit parent class
# todo: have to read the net to be able to define it as abstract
class SimCockpit(Daemon):
	
	# config settings
	host = '127.0.0.1'
	port = 50007

	# helper objects
	logging = False

	# private
	socket = False

	def init(self, logging = False):
		self.setLogging(logging)
		
	# set host ip to run listener socket on	
	def setHost(self, host):
		self.host = host

	# set port to run listener socket on
	def setPort(self, port):
		self.port = int(port)

	# set logging object for debug purpose
	def setLogging(self, logging):
		self.logging = logging

	# create listener socket
	def initListenerSocket(self):
		# main listener for game input
		if self.socket == False:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# listen on main port for game input
			self.socket.bind((self.host, self.port))
			self.socket.listen(5)

	# accept connections
	def accept(self):
		(connection, address) = self.socket.accept()
		data = True
		while data:
			data = connection.recv(4096)
			self.process(data)		

	# main loop
	def run(self):
		self.initListenerSocket()
		while True:
			#accept connections from outside
			self.accept()

	# todo: overwrite stop method, close sockets and call parent stop

	# overwrite this method and process your data
	# todo: should be abstract as well, make sure its re-implemented in child classes
	def process(self, data):
		# overwrite this function
		print data