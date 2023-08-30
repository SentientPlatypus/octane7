import os
import pprint
import pygame
import threading

mappings = {
    "button5":"boost",
    "button4":"slide/ar",
    "axis6":"movement",
    "axis0":"sx",
    "axis1":"sy",
    "axis3":"cx",
    "axis4":"cy",
    "button0":"jump",
    "button1":"arl",
    "button2":"arr",
    "button3":"y"
    
    
    
}


class Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    def __init__(self):
        """Initialize the joystick components"""

        self.input_data = {}
        for key in mappings.keys():
            self.input_data[mappings[key]] = 0
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        
        self._monitor_thread = threading.Thread(target=self.listen, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        
    def listen(self):
        """Listen for events to happen"""
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 5:
                        # Left trigger
                        self.input_data["RightTrigger"] = (round(event.value) + 1) / 2
                    elif event.axis == 2:
                        # Right trigger
                        self.input_data["LeftTrigger"] = (round(event.value) + 1) / 2
                    else:
                        self.input_data[mappings[f"axis{event.axis}"]] = round(event.value, 4)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.input_data[f"button{event.button}"] = 0
                elif event.type == pygame.JOYBUTTONUP:
                    self.input_data[mappings[f"button{event.button}"]] = 0
                elif event.type == pygame.JOYHATMOTION:
                    self.input_data[f"hat{event.hat}"] = event.value

                
    def read(self):
        return self.input_data

def controller_main():
    xboxc = Controller()
    xboxc.init()
    while 1:
        print(xboxc.read())

controller_main()
