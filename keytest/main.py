import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a CircuitPlayground Express' A and B buttons.
swap = digitalio.DigitalInOut(board.GP5)
swap.direction = digitalio.Direction.INPUT
swap.pull = digitalio.Pull.DOWN


while True:
    # press ALT+TAB to swap windows
    if swap.value:
        kbd.send(Keycode.N)
        kbd.send(Keycode.E)
        time.sleep(.02)
        kbd.send(Keycode.Y)
        kbd.send(Keycode.O)
        time.sleep(.02)
        kbd.send(Keycode.ENTER)
        time.sleep(0.5)

    # press CTRL+K, which in a web browser will open the search dialog
    time.sleep(0.1)
