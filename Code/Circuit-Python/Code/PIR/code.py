import time
import board, digitalio

PIR = digitalio.DigitalInOut(board.PIR)
PIR.direction = digitalio.Direction.INPUT

LED = digitalio.DigitalInOut(board.D1) #place an LED on pin 1
LED.direction = digitalio.Direction.OUTPUT

while True:
   if PIR.value == True:
        LED.value = True
        time.sleep(2)
   else:
        LED.value = False
       

 