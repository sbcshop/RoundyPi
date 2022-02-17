from machine import Pin, I2C, UART,SPI
import utime
import pmsa003

import random
import gc9a01
import italicc

import vga1_bold_16x32 as font
import vga1_bold_16x16 as font1

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))


spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = gc9a01.GC9A01(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=2)
tft.init()
tft.fill(gc9a01.BLACK)
utime.sleep(0.5)
tft.text(font, "RP2040 Round", 20, 50, gc9a01.RED)
tft.text(font, "Display Board 1.28", 20, 80, gc9a01.YELLOW)
tft.text(font, "1.28(240x240)", 20, 120, gc9a01.BLUE)
tft.text(font, "AIR MONITOR", 20, 150, gc9a01.GREEN)
utime.sleep(2) 
tft.fill(gc9a01.BLACK)




# Methods
# ---------------------------------------------------------------------------
def read_value(sensor):
    """Read a sensor value and store it in the database."""
    # Read the value from the sensor.
    reading = sensor.read()
    #now = datetime.utcnow()
    
    print(" pm10: {:d} pm25: {:d} pm100: {:d}" .format(reading.pm10_cf1, reading.pm25_cf1, reading.pm100_cf1))
    #oled.text("PM1.0= {:2d}".format(reading.pm10_cf1),5,5)
    tft.text(font,"PM1.0= {:2d}".format(reading.pm10_cf1), 25, 40, gc9a01.YELLOW)

    #oled.show()
    #oled.text("PM2.5= {:2d}".format(reading.pm25_cf1),5,15)
    tft.text(font,"PM2.5= {:2d}".format(reading.pm25_cf1), 25, 80, gc9a01.YELLOW)

    #oled.show()
    #oled.text("PM10.0= {:2d}".format(reading.pm100_cf1),5,25)
    tft.text(font, "PM10.0= {:2d}".format(reading.pm100_cf1), 25, 120, gc9a01.YELLOW)

    #oled.show()
    #oled.text("S",120,0)
    #oled.show()
  
  
sensor = pmsa003.Sensor("0")    
utime.sleep(2)    
        
while True:
        read_value(sensor)
        utime.sleep(2) #delay of two sec

