# Flashing Circuit Python Firmware onto your board.

put the board into download mode by holding boot button and pressing reset button then release both buttons. 
Use esptool to erease flash and then flash new firmware onto the board.

##Erase the flash.

### Windows
Change xxx to whatever COM port is being used by the board
```bash
esptool --chip esp32s2 --port COMxxx erase_flash
```
### Linux
```bash
esptool.py --chip esp32s2 --port /dev/ttyACM0 erase_flash
```

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
```bash
esptool.py --chip esp32s2 --port /dev/cu.usbmodem01 erase_flash
```
_____________________________________________________________________________________________

## Flash New Firmware To The Board

### Windows
````
esptool.py --chip esp32s2 -p COMxxx  -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x1000 bootloader.bin 0x2d0000 tinyuf2.bin
````

### Linux
```bash
esptool.py --chip esp32s2 -p /dev/ttyACM0 -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x1000 bootloader.bin 0x2d0000 tinyuf2.bin
```

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
```bash
esptool.py --chip esp32s2 -p /dev/cu.usbmodem01 -b 460800 --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size 4MB 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x1000 bootloader.bin 0x2d0000 tinyuf2.bin
```

Once that is done you should see a new flash drive show up called BMBOOT. 

Open that up and drag the firmware.uf2 file onto it. 

The BMBOOT drive will disappear for a few seconds and then come back as CIRCUITPY. 

You're now good to use circuit python on the board!
