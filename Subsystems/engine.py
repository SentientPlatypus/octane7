import RPi.GPIO as GPIO
import threading


class Engine(object):

    def __init__(self, controller, en, in1, in2) -> None:
        print("ENGINE INITIALIZATION".center(20, "-"))
        self.controller = controller
        self.en = en
        self.in1 = in1
        self.in2 = in2
        print("initialized pins")

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        self.p=GPIO.PWM(en,1000)
        print("initialized GPIO")
        

        self._monitor_thread = threading.Thread(target=self._monitor_engine, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        print("monitor thread started")

    def _monitor_engine(self):
        print("monitoring")
        self.p.start(0)
        print("pwm started")
        while 1:
            values = self.controller.read()
            if values["y"]:
                self.p.stop()
                GPIO.cleanup()
                print("GPIO Clean up")
                break

            movement = values["movement"]
            self.p.ChangeDutyCycle(abs(movement) * 100)
            if movement > 0:
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
                print("forward")
            elif movement < 0:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
                print("backward")
            else:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.LOW)   


if __name__ == "__main__":
    from baseinputs import Controller
    import signal
    xboxWireless = Controller()
    en = 22
    in1 = 17
    in2 = 27
    GPIO.setwarnings(False)    
    e = Engine(xboxWireless, en, in1, in2)
    while 1:
        pass
    
