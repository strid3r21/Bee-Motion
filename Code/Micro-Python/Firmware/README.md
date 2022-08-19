# How to flash the Micro Python Firmware onto the Bee Motion


Put the board into download mode by holding boot button and pressing reset button then release both buttons. 
Use esptool to erease flash and then flash new firmware onto the board.

## Erase the flash.

### Linux
```bash
esptool.py --chip esp32s2 --port /dev/ttyACM0 erase_flash
```

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
```bash
esptool.py --chip esp32s2 --port /dev/cu.usbmodem01 erase_flash
```

### Windows
Change xxx to whatever COM port is being used by the board
```bash
esptool --chip esp32s2 --port COMxxx erase_flash
```

## Now flash the firmware on to the board.

### Linux
```bash
esptool.py --chip esp32s2 -p /dev/ttyACM0 write_flash -z 0x1000 firmware.bin
```

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
```bash
esptool.py --chip esp32s2 -p /dev/cu.usbmodem01 write_flash -z 0x1000 firmware.bin
```

### Windows
Change xxx to whatever COM port is being used by the board
```bash
esptool.py --chip esp32s2 -p COMxxx write_flash -z 0x1000 firmware.bin
