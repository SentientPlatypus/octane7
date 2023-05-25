from gpiozero import Motor
from getINPUTS import XboxController

class Subsystem():
    def periodic():
        ...

class boost(Subsystem):
    
    def __init__(self, controller:XboxController, pin) -> None:
        self.motor:Motor = Motor(*pin)
        
    def periodic(self):
        if self.motor.read["boost"]:
            self.motor.forward(1)
    