#!/usr/bin/env python
from SimCockpit import SimCockpit
import socket
import time

# SimCockpit main process, listen to game data and passes to roll/pitch servers
class SimCockpitMain(SimCockpit):

	# client socket for roll
	socketRoll = False
	# client socket for pitch
	socketPitch = False
	# clients array to connect
	clients = []

	# set array of client config objects
	def setClients(self, clients):
		self.clients = clients

	# connect as client to roll/pitch servers
	def initClientSockets(self):
		if  len(self.clients) == 0:
			self.logging.debug("SimCockpit main daemon need to have clients settings.")
			sys.exit(2)

		for client in self.clients:
			if client['SOCKET'] == False:
				client['SOCKET'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# connect until connected
			self.logging.debug('Try connecting to ', client['HOST'])
			clientConnected = False
			
			while clientConnected != True:
				try:
					client['SOCKET'].connect((client['HOST'], int(client['PORT'])))
					clientConnected = True
					self.logging.debug('Connected to client %s  on port  %s.' % (client['HOST'], client['PORT']))
				except socket.error, e:
					clientConnected = False
					self.logging.debug('Could not connect to client %s  on port  %s. Next try in one second' % (client['HOST'], client['PORT']))
					time.sleep(1)
				pass

			# store sockets as class properties
			if client['TYPE'] == 'roll':
				self.socketRoll = client['SOCKET']

			if client['TYPE'] == 'pitch':
				self.socketPitch = client['SOCKET']

	# overwrite initListenerSocket cause the main Process needs to connect to both server
	def initListenerSocket(self):
		self.initClientSockets()
		super(SimCockpitMain, self).initListenerSocket()

	# process data, split and pass to roll/pitch servers
	def process(self, data):
		lines = data.split("\n")
		for line in lines:
			if  line != '':
				values = line.split('|')
				for value in values:
					label_and_value = value.split(':')
					if len(label_and_value) == 2:
						label = label_and_value[0]
						value = label_and_value[1]
						if label == 'Roll':
							self.socketRoll.send(value)
						elif label == 'Pitch':
							self.socketPitch.send(value)