from Subsystems import baseinputs, engine, steering

class constants():
    "ENGINE PINS"
    en = 22
    in1 = 17
    in2 = 27

    "STEERING PINS"
    steering_pwm = 16

class octane(object):

    def __init__(self) -> None:
        self.controller = baseinputs.Controller()
        self.engine = engine.Engine(self.controller, constants.en, constants.in1, constants.in2)
        self.steering = steering.Steering(self.controller, constants.steering_pwm)






