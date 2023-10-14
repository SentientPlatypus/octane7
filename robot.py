from Subsystems import baseinputs, engine, steering, boost

class constants():
    "ENGINE PINS"
    en = 17
    in1 = 27
    in2 = 22

    "STEERING PINS"
    steering_pwm = 16

    "BOOSTER PINS"
    in3 = 23
    in4 = 24

class Octane(object):

    def __init__(self) -> None:
        self.controller = baseinputs.Controller()
        self.engine = engine.Engine(self.controller, constants.en, constants.in1, constants.in2)
        self.steering = steering.Steering(self.controller, constants.steering_pwm)
        self.booster = boost.Booster(self.controller, constants.in3, constants.in4)


if __name__ == "__main__":
    octanecar = Octane()


