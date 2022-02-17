#
# gc9a01_picture_locket.py -- Simple Demo of GC9A01 Round LCD 
#
# 2021 - Tod Kurt - todbot.com
#
# Tested on QTPy (SAMD21), QTPy RP2040, and Raspberry Pi Pico (RP2040)
# running CircuitPython 7.
#
# You'll need to install 'gc9a01' package.
# Easiest way to do this is from Terminal:
#  circup install gc9a01
#

import time
import board
import math
import busio
import terminalio
import displayio
import adafruit_imageload
import gc9a01

# prepare image with ImageMagick like:
# convert input.jpg -resize 240x240 -type palette BMP3:output.bmp
img_filenames = ( "/images/img0.bmp","/images/img1.bmp","/images/img2.bmp","/images/img3.bmp")

# time in seconds between images
img_time = 2

# Release any resources currently in use for the displays
displayio.release_displays()

# attempt to auto-detect board type
import os
board_type = os.uname().machine
if 'Pico' in board_type:
    # Raspberry Pi Pico pinout, one possibility, at "southwest" of board
    tft_clk = board.GP10 # must be a SPI CLK
    tft_mosi= board.GP11 # must be a SPI TX
    tft_rst = board.GP12
    tft_dc  = board.GP8
    tft_cs  = board.GP9
    tft_bl  = board.GP13
    spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)
else:
    print("ERROR: Unknown board!")
    
# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

# Make the main display context
main = displayio.Group()
display.show(main)

i=0
while True:
    #print(time.monotonic(),"hello")
    img_filename = img_filenames[i]
    img_bitmap = displayio.OnDiskBitmap(open(img_filename, "rb"))
    img_palette = displayio.ColorConverter()
    #img_bitmap, img_palette = adafruit_imageload.load(img_filename)
    img_tilegrid = displayio.TileGrid(img_bitmap, pixel_shader=img_palette)
    main.append(img_tilegrid)
    time.sleep(img_time)
    main.pop()  # remove image
    i = (i+1) % len(img_filenames)  # go to next file
    

    
