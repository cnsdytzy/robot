robot
=====

Tri-omni-wheel robot control and drive code

To Drive bot:
1. load arduino with basicdrive.ino code
2. leave usb cord connected for serial data transmission
3. connect a joystick
4. run control.py

Controls:
	 Hat controls:
	 	up: move robot north
		down: south
		left: west
		right: east
	button controls:
		2: turn left
		3: turn right
		0 (trigger): stop
	keyboard:
		press return when inside of python.app to exit program
		
Additional:
	- sensors do nothing currently
	- requires pygame, and pyserial
	
