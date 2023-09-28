import RPi.GPIO as GPIO
import threading

def map_range(value, from_min, from_max, to_min, to_max):
    # Calculate the percentage of value's position in the from range
    percentage = (value - from_min) / (from_max - from_min)
    
    # Map the percentage to the to range and return the result
    mapped_value = to_min + percentage * (to_max - to_min)
    return mapped_value

class Steering():
    def __init__(self, controller, pwm) -> None:
        self.controller = controller

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm, GPIO.OUT)
        self.servo = GPIO.PWM(pwm)

        self._monitor_thread = threading.Thread(target=self._monitor_steering, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    
    def _monitor_steering(self):
        values = self.controller.read()
        sx = values["sx"]

        duty = map_range(sx, -32000, 32000, 2, 12)
        self.servo.ChangeDutyCycle(duty)

if __name__ == "__main__":
    import signal
    from baseinputs import Controller
    import signal
    xboxWireless = Controller()
    pwm = 19
    GPIO.setwarnings(False)    
    s = steering(xboxWireless, pwm)
    while 1:
        pass
    




