#!/usr/bin/python
from ControllerInput.baseinputs import Controller
import RPi.GPIO as GPIO



en = 22
in1 = 17
in2 = 27


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