import RPi.GPIO as GPIO
import threading


class Booster(object):

    def __init__(self, controller, in3, in4) -> None:
        self.controller = controller
        self.in3 = in3
        self.in4 = in4

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in3, GPIO.OUT)
        GPIO.setup(in4, GPIO.OUT)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

        self._monitor_thread = threading.Thread(target=self._monitor_boost, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        print("BOOSTER INITIALIZED".center(50, "-"))

    def _monitor_boost(self):
        while 1:
            values = self.controller.read()

            if values["y"]:
                self.p.stop()
                GPIO.cleanup()
                print("GPIO Clean up")
                break

            boost = values["boost"]
            if boost:
                GPIO.output(self.in3,GPIO.HIGH)
                GPIO.output(self.in4,GPIO.LOW)
            else:
                GPIO.output(self.in3,GPIO.LOW)
                GPIO.output(self.in4,GPIO.LOW)   


if __name__ == "__main__":
    import signal
    from baseinputs import Controller
    import signal
    xboxWireless = Controller()
    in1 = 23
    in2 = 24
    GPIO.setwarnings(False)    
    e = Booster(xboxWireless, in1, in2)
    while e._monitor_thread.is_alive():
        pass
    
