#! /usr/bin/python
import pygame
import serial

connection = serial.Serial(port='/dev/tty.usbmodem411', baudrate=9600)


def readButton(action):
    button = action['button']
    print 'Button',button
    if button == 2:
        print 'LEFT'
        connection.write('L')
    elif button == 3:
        print 'RIGHT'
        connection.write('R')
    elif button == 1:
        print 'HALT'
        connection.write('H')
    elif button == 0:
        print 'HALT'
        connection.write('H')
    

def readAxis(action):
    print 'Axis',action['axis'],'=',action['value']

def readHat(action):
    position = action['value']
    print 'Hat',position
    if position == (0,0):
        print 'HALT'
        connection.write('H')
    elif position == (1,0):
        print 'EAST'
        connection.write('E')
    elif position == (-1,0):
        print 'WEST'
        connection.write('W')
    elif position == (0,-1):
        print 'SOUTH'
        connection.write('S')
    elif position == (0,1):
        print 'NORTH'
        connection.write('N')


def readKey(action):
    print 'Key',action['unicode']
    if action['unicode'] == u'r':
        connection = serial.Serial(port='/dev/tty.usbmodem411', baudrate=9600)
    elif action['unicode'] == u'\r':
        bye()

def printDisplay():
    print display()

def updateDisplay(tuple):
    display[tuple[0]] = tuple[1]

def actionListener():
    while True:
        action = pygame.event.wait()
        if action.type == pygame.JOYAXISMOTION:
            #readAxis(action.dict)
            pass
        elif action.type == pygame.JOYHATMOTION:
            readHat(action.dict)
        elif action.type == pygame.JOYBUTTONDOWN:
            readButton(action.dict)
        elif action.type == pygame.KEYDOWN:
            readKey(action.dict)


def bye():
    connection.close()
    exit()

def main():
    pygame.joystick.init()  
    pygame.display.init()
    if (pygame.joystick.get_count() < 1):
        print 'please connect a joystick and try again'
        exit()
    device = pygame.joystick.Joystick(0)
    print 'Using',device.get_name()
    device.init()
    print "Press 'return' to exit"
    actionListener()

if __name__ == "__main__":  
    main()