import time
from machine import Pin
import bm

PIR = Pin(bm.PIR, Pin.IN, Pin.PULL_UP) #setup the PIR Pin
LED = Pin(1, Pin.OUT) # put an LED on pin 1

while True:
    motion = PIR.value() #motion equals whatever the PIR is reading
    if motion == True: # if motion is detected - turn on the LED
        LED.value(1)
    else:               # if no motion, turn off the LED
        LED.value(0)


