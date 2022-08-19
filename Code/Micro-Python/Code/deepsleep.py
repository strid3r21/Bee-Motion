from time import sleep
import esp32
from machine import Pin, deepsleep
from time import sleep
import bm #import the bee motion helper library

# set the wake up PIR Sensor to be pin in and name it wake1
wake1 = Pin(bm.PIR, mode = Pin.IN)

# set the wake up source to be the PIR motion sensor
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ANY_HIGH)


print('Im awake, but Im going to sleep in 10 seconds')
sleep(10)

# The reason we can get away with a much lower sleep time here unlike in the main.py
# example is because once you import this code to the board, it will only run though
# 1 loop. ie, import the sketch. it goes to sleep and then wakes up, but it will not
# continue to run this code unless its imported again. To have code run automatically
# on boot, put your code in the main.py 

deepsleep()