#!/usr/bin/python
from ControllerInput.baseinputs import Controller
import RPi.GPIO as GPIO
import threading


en = 22
in1 = 17
in2 = 27


class Engine(object):

    def __init__(self, controller, en, in1, in2) -> None:
        self.controller = controller
        self.en = en
        self.in1 = in1
        self.in2 = in2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        self.p=GPIO.PWM(en,1000)

        self._monitor_thread = threading.Thread(target=self._monitor_engine, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def _monitor_engine(self):
        while 1:
            values = self.controller.read()

            if values["y"]:
                self.p.stop()
                GPIO.cleanup()
                print("GPIO Clean up")
                break

            movement = values["movement"]
            self.p.ChangeDutyCycle(abs(movement))
            if movement > 0:
                GPIO.output(self.in1,GPIO.HIGH)
                GPIO.output(self.in2,GPIO.LOW)
                print("forward")
            else:
                GPIO.output(self.in1,GPIO.LOW)
                GPIO.output(self.in2,GPIO.HIGH)
                print("backward")


if __name__ == "__main__":
    xboxwireless = Controller()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    p=GPIO.PWM(en,1000)



    while 1:
        values = xboxwireless.read()

        if values["y"]:
            p.stop()
            GPIO.cleanup()
            print("GPIO Clean up")
            break

        movement = values["movement"]
        p.ChangeDutyCycle(abs(movement))
        if movement > 0:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            print("forward")
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            print("backward")