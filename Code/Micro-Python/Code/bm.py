# THIS FILE IS A HELPER LIBRARY FOR THE BEE MOTION. 
# IT IS BAKED INTO THE FIRMWARE. 
# YOU DONT NEED TO PUT IT ON YOUR BOARD.
# ITS HERE FOR YOUR REFERENCE ONLY.

# Import required libraries
from micropython import const

BOOT_BTN = const(0)
PIR = const(5)


# SPI
SPI_MOSI = const(14)
SPI_MISO = const(15)
SPI_CLK = const(16)

# I2C
I2C_SDA = const(37)
I2C_SCL = const(36)

