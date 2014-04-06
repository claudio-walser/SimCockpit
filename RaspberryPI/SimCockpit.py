#!/usr/bin/python
import sys
import logging
import ConfigParser

from lib.Daemon import Daemon
from lib.SimCockpitMain import SimCockpitMain
from lib.SimCockpitRoll import SimCockpitRoll
from lib.SimCockpitPitch import SimCockpitPitch

# configuration
config = ConfigParser.ConfigParser()
config.read('config.cfg')

# read daemon type, take main as default
daemon = 'main'
if len(sys.argv) == 3:
	if sys.argv[2] in ['main', 'roll', 'pitch']:
		daemon = sys.argv[2]

# read main configuration
PIDFILE = config.get(daemon, 'PIDFILE')
LOGFILE = config.get(daemon, 'LOGFILE')
HOST = config.get(daemon, 'HOST')
PORT = config.get(daemon, 'PORT')

# main daemon has roll and pitch daemon as client
if daemon == 'main':
	CLIENTS = [
		{
			'HOST': config.get('roll', 'HOST'),
			'PORT': config.get('roll', 'PORT'),
			'SOCKET': False,
			'TYPE': 'roll'
		}, {
			'HOST': config.get('pitch', 'HOST'),
			'PORT': config.get('pitch', 'PORT'),
			'SOCKET': False,
			'TYPE': 'pitch'
		}
	]
else:
	CLIENTS = []


# Configure logging
logging.basicConfig(filename=LOGFILE,level=logging.DEBUG)
logging.captureWarnings(True)

# main loop
if __name__ == "__main__":

	# instantiate daemon and setup socket
	if daemon == 'main':
		simCockpit = SimCockpitMain(PIDFILE)
		simCockpit.setClients(CLIENTS)
	elif daemon == 'roll':
		simCockpit = SimCockpitRoll(PIDFILE)
	elif daemon == 'pitch':
		simCockpit = SimCockpitPitch(PIDFILE)
	else:
		print "Unknown daemon: ", daemon
		sys.exit(2)

	# start|stop|restart|status
	if len(sys.argv) >= 2:
		# start daemon
		if 'start' == sys.argv[1]:
			print "Starting ..."
			try:
				 # set host and port for listener socket
				simCockpit.init(logging)
				simCockpit.setHost(HOST)
				simCockpit.setPort(PORT)
				simCockpit.start()
			except:
				pass
		# stop daemon
		elif 'stop' == sys.argv[1]:
			print "Stopping ..."
			simCockpit.stop()
		# restart daemon
		elif 'restart' == sys.argv[1]:
			print "Restaring ..."
			simCockpit.restart()
		# show status
		elif 'status' == sys.argv[1]:
			try:
				pf = file(PIDFILE, 'r')
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
	else:
		print "usage: %s start|stop|restart|status %s" %(sys.argv[0], daemon)
		sys.exit(2)


