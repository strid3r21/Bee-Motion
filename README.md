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

## Add the Espressif ESP32 arduino board library to Arduino IDE
File > Preferences > at the bottom "Additional Board Manager URLS" paste in this url
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json 
 
From there you will be able to search and add the ESP32 board library from the board library search bar. install the ESP32 library by Espressif and make sure you're using version number 2.0.5 or later. You will then be able to select your Bee Motion from the board manager.

## How to program the Bee Motion
In order to program the Bee Motion you need to put it into download mode. To do so all you need to do is connect the USB-C cable and then press and hold the boot button. with the boot button being held down, press the reset button and release. then you can release the boot button. this will put the Bee Motion into download mode which will allow it to be programmed. Then for the board, select "Bee Motion" from the board manager.


# Battery Life Information
_______________________________________________________________________________________________________________________

**On battery power the Bee Motion uses about 80mAH while on WiFi**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Awake%20Bat.jpg?raw=true)

**During deepsleep it uses about 45uA!**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Deep%20Sleep%20Bat.jpg?raw=true)

**For sake of an example, if paired with a 1500mAh LiPo battery and triggered 20x a day with Wifi it would last for over a year!**
![alt text](https://github.com/strid3r21/Bee-Motion/blob/main/Battery%20Info/Bee%20Motion%20Battery.png?raw=true)

