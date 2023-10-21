from gpiozero import Servo
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
        self.servo = Servo(pwm, min_pulse_width=0.0006, max_pulse_width=0.0024, frame_width= 5/1000)

        self._monitor_thread = threading.Thread(target=self._monitor_steering, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()
        print("STEERING INITIALIZED".center(50, "-"))

    
    def _monitor_steering(self):
        while 1:
            values = self.controller.read()
            if values["y"]:
                self.servo.stop()
                GPIO.cleanup()
                print("GPIO cleanup")
                break
            sx = values["sx"]
            duty = map_range(sx, -1, 1, -1, 1)
            self.servo.value = duty

if __name__ == "__main__":
    from baseinputs import Controller
    xboxWireless = Controller()
    pwm = 16
    GPIO.setwarnings(False)    
    s = Steering(xboxWireless, pwm)
    while s._monitor_thread.is_alive():
        pass
    




