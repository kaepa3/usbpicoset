import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices)

input_list = [board.GP10, board.GP11]
power_list = [board.GP20, board.GP21]


def create_power_pin(list):
    powers = []
    for v in list:
        pin = digitalio.DigitalInOut(v)
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = False
        powers.append(pin)
    return powers


def create_input_pin(list):
    inputs = []
    for p in list:
        pin = digitalio.DigitalInOut(p)
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.DOWN
        inputs.append(pin)
    return inputs


powers = create_power_pin(power_list)
inputs = create_input_pin(input_list)

status = [[False] * len(powers) for i in range(len(inputs))]

print("start")
while True:
    keyon = []
    for power_index, power in enumerate(powers):
        power.value = True
        for input_index, input in enumerate(inputs):
            if input. value != status[power_index][input_index]:
                print("{0},{1}:is {2}".format(
                    power_index, input_index, "on" if input.value else "off"))
                status[power_index][input_index] = input.value
        power.value  = False

    time.sleep(0.1)
