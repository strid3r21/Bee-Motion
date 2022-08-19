# any code put in this main.py file will run automatically on the board,
# even after a reset. 


from time import sleep
import esp32
from machine import Pin, deepsleep
from time import sleep
import bm #import the bee motion helper library

# set the wake up PIR Sensor to be pin in and name it wake1
wake1 = Pin(bm.PIR, mode = Pin.IN)

# set the wake up source to be the PIR motion sensor
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)


print('Im awake, but Im going to sleep in 60 seconds')
# VERY IMPORTANT - set the sleep (ie, delay) to minimum 60 seconds.
# if this is set to a low number like 5, then if you need to change the code
# and re-upload it to the board, the board will go to sleep too quickly
# before you can get the new code uploaded. the only way to fix it in
# that scenario is to reflash the micropython firmware to the board.
sleep(60)

deepsleep()