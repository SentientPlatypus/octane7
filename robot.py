from Subsystems.baseinputs import Controller
from Subsystems.engine import Engine

class constants():
    en = 22
    in1 = 17
    in2 = 27

class octane(object):

    def __init__(self) -> None:
        self.controller = Controller()
        self.engine = Engine(self.controller, constants.en, constants.in1, constants.in2)






