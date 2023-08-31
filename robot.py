from Subsystems import baseinputs, engine

class constants():
    en = 22
    in1 = 17
    in2 = 27

class octane(object):

    def __init__(self) -> None:
        self.controller = baseinputs.Controller()
        self.engine = engine.Engine(self.controller, constants.en, constants.in1, constants.in2)






