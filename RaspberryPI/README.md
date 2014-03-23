# SimCockpit
Just put the SimCockpit.py in any favorite folder to execute and install the dependencies on your system.
The socket server will listen on 10.20.0.122:50007 currently. Change that to your needs if you want.

## Dependencies
 - python >= 2.5.x
 - [python-daemon](https://github.com/martinrusev/python-daemon/ "python-daemon") for daemonizing the socket server.
 - python-setuptools for installing python-daemon properly. On Raspbian just do 
    apt-get install python-setuptools

## Installation
Just copy the SimCockpit.py to any directory you want and make it executable.

## Usage
    python /Path/To/Your/CodeBase/SimCockpit.py (start|stop|restart|status)