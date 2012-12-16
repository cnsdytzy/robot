import socket
import pygame

QUIT_ACTIONS = [{'scancode': 12, 'key': 113, 'unicode': u'q', 'mod': 1024}, {}]

class UDPConnection:
    def __init__(self, config):
        self.address = config['address']
        self.port = config['port']
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def write(self, message):
        sock.sendto(message, (self.address, self.port))


class ControlDisplay:
    def __init__(self, controls, ui):
        self.controllerState = {}
        self.stick = None
        
        self.screen = None
        
        
    
    def _setupDisplay(self, height, width, fullscreen):
        pygame.display.init()
        self.screen = pygame.display.set_mode((width, height))
        
        background = pygame.Surface(screen.get_size()).convert()
        background.fill((250, 250, 250))
        
        pygame.display.set_caption('Robot Drive')
        
        pygame.font.init()

        
    def _setupControls(self):
        if (pygame.joystick.get_count() > 0):
            self.stick = pygame.joystick.Joystick(0)
            self.stick.init()
            
        
    def updateDisplay(self):
        screen.fill((255,255,255))
        screen.blit(font.render(str(axesValues), 1, (10, 10, 10)),(10,10))
        pygame.display.flip()

            
    def controlInput(self):
        event = pygame.event.wait()
        action = event.__dict__
        
        if 'axis' in action:    
            
        
            
        elif 'hat' in action:
            
            
            
            
        elif 'button' in action:
            
            

        elif action in QUIT_ACTIONS:
            exit()
        
        
        
class Axis:
    def __init__(self, name, outputMaximum = 128, inputMaximum = 128):
        self.name = name
        self.value = 0
        self.inputMaximum = 0.01
        self.inputMinimum = -0.01
        self.outputMaximum = outputMaximum
        self.inputMaximum = inputMaximum

    def calibrate(self, input):
        if value > 0 and value > self.inputMaximum:
            self.inputMaximum = value

        elif value < 0 and value < self.inputMinimum:
            self.inputMinimum = value
        
    def update(self, input):
        self.value = input

    def read(self):
        self.value
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        