from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
gamepad = InputDevice('/dev/input/event6')
print(gamepad)
input("continue")

rawinputs = {}
inputs = {}

codetoval = {"0":"sx", "1":"sy", "5":"gas", "2":"brake","311":"boost", "3":"cx", "4":"cy", "304":"jump", "307": "arr", "305":"arl", "310":"ar/drift"}


for key in codetoval.keys():
    inputs[codetoval[key]] = 0
print(inputs)
for event in gamepad.read_loop():
    rawinputs[str(event.code)] = event.value
    #inputs[codetoval[str(event.code)]] = event.value
    print(rawinputs)