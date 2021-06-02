import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices)

pin_list = [
    board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
    board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,
    board.GP21, board.GP22, board.GP25,
    board.GP26,
]


def create_value(list):
    values = []
    pins = []
    for i, p in enumerate(pin_list):
        swap = digitalio.DigitalInOut(p)
        swap.direction = digitalio.Direction.INPUT
        swap.pull = digitalio.Pull.DOWN
        pins.append(swap)
        values.append(swap.value)

    return values, pins


values, pins = create_value(pin_list)

print("loop start:{0}".format(len(pin_list)))
while True:
    # press ALT+TAB to swap windows
    for idx, pin in enumerate(pins):
        if pin.value != values[idx]:
            tm = time.time()
            print("{0}=>{1}".format(idx+1, "on" if pin.value else "off"))
        values[idx] = pin.value

    # press CTRL+K, which in a web browser will open the search dialog
    time.sleep(0.1)
