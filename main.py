import time
import usb_hid
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

while True:
    m.move(x=100)
    time.sleep(1)
