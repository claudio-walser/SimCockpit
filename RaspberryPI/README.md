# SimCockpit

## What the heck i am trying to do
Its simple i want a cage to sit in, play flight simulator and make every movement the plane does in my cage.
As a "proof of concept" and "ask for an offer" i built the thing with around 50cm to 30cm to 15cm, means a small model.

## Rough concept since this is eeeeeeeeaaaaaaarly alpha stuff
Just put the SimCockpit.py in any favorite folder to execute and install the dependencies on your system.
The socket server will listen on 10.20.0.90:50007 for game input currently. Change that to your needs if you want.
The main daemon is expecting yaw and pitch values at once, its extracting both values and passing each to a different raspberry via socket on port 50008. Those clients then control a stepper motor each.
Two because for my model i dont want to wire up all the stuff for rotary, its easier to place one raspi inside the cage.

## Dependencies
 - python >= 2.5.x
 - [python-daemon](https://github.com/martinrusev/python-daemon/ "python-daemon") for daemonizing the socket server.
 - python-setuptools for installing python-daemon properly. On Raspbian just do 
    apt-get install python-setuptools

## Installation
Just copy the SimCockpit.py to any directory you want and make it executable.

## Usage
    python /Path/To/Your/CodeBase/SimCockpit.py (start|stop|restart|status)
