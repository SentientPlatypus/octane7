#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

direction = int(input('Please define the direction (Left=1 or Right=2): '))
dc = int(input('Please define the Motor PWM Duty Cycle (0-100): '))
hz = int(input ('HZ: '))
pwm = GPIO.PWM(17, hz)

if direction == 1:
	GPIO.output(27, 1)
	GPIO.output(22, 0)
elif direction == 2:
	GPIO.output(27, 0)
	GPIO.output(22, 1)

try:
        while True:
                pwm.start(dc)

except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()