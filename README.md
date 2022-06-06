# Bee Motion


## **Visit our** [Discord](https://tinyurl.com/Bee-Motion-Discord-Git)
## **Buy on** [Tindie](https://www.tindie.com/products/smartbee/bee-motion-esp32-pir-motion-sensor/)
________________________________________________________________________________________________________________________


# Video Overview
[<img src="https://img.youtube.com/vi/eUtSaV774to/maxresdefault.jpg" width="100%">](https://youtu.be/eUtSaV774to)
________________________________________________________________________________________________________________________

# Pinouts
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Bee-Motion-Info-Card.png?raw=true)
________________________________________________________________________________________________________________________

# TroubleShooting Tips

## How to program the Bee Motion
In order to program the Bee Motion you need to put it into download mode. To do so all you need to do is connect the USB-C cable and then press and hold the boot button. with the boot button being held down, press the reset button and release. then you can release the boot button. this will put the Bee Motion into download mode which will allow it to be programmed. Then for the board, select the ESP32S2 Dev Module.

## My Computer only will see the Bee Motion when its in download mode.
Go to Tools > USB CDC on Boot and make sure that is enabled. Once it's enabled, reflash your code to the Bee Motion and your PC will see the Bee Motion when its plugged in and the Serial Monitor will work. Connect board to PC, open serial monitor in Arduino IDE and then hit reset on the board should initialize the serial monitor for debugging.

![alt text](https://imgur.com/Zo4XGVt.jpg?raw=true)


# Battery Life Information
_______________________________________________________________________________________________________________________

**On Battery the Bee Motion Uses about 80mAH while on WiFi**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Awake%20Bat.jpg?raw=true)

**During Deepsleep it uses about 45uA!**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Deep%20Sleep%20Bat.jpg?raw=true)

**For sake of an example, if paired with a 1500mAh LiPo battery and triggered 20x a day with Wifi it would last for over a year!**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Battery.png?raw=true)

