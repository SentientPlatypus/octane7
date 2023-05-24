from gpiozero import Motor
from getINPUTS import XboxController

class boost():
    
    def __init__(self, controller:XboxController, pin) -> None:
        self.motor:Motor = Motor(*pin)
        
    def periodic(self):
        if self.motor.read["boost"]:
            self.motor.forward(1)
    