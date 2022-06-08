## RoundyPi
### RoundyPi is a round LCD display based on RP2040 along with a compact and stylish 1.28-inch display module of 240×240 resolution, 65K RGB colors, clear and colorful displaying effect, expand its engagement with your project. RoundyPi comes with an embedded GC9A01 Driver and SPI Interface that minimize the required IO pins. 
<img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img7.png" />

See there is a folder name RoundyPi, inside this folder, there are various applications:-
In this device we use Micropython and Circuit python(Adafruit Industries) both 

  * **Connect Air Monitoring Sensor (use breakout)** -> (Use Micropython) We add the four GP pins for Input/Output devices(GP0,GP1,GP2,GP3).For example, We connect Air monitoring breakout,         save this file "pmsa003.py" in the pico, this is the library of the air monitor sensors. and for round LCD you need to drag and drop the round LCD firmware "firmware.uf2".       for this first you need to press the boot button then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named         "RPI-RP2" drag this file "firmware.uf2" to this device as shown in figure 
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img6.png" />

  * **Display Images** -> For display images, I use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit         python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). for this first you need to press the boot button then connect      the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this file 
    "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2" to this device as shown in figure:
    this is the official website, or yoy can download from here https://circuitpython.org/board/raspberry_pi_pico/
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />  
    When you properly insert the circuitpython then you see a new device that looks like the below image:-
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />  
    Now open the folder Display_Images, which is inside the RoundyPi folder, inside the Display_Images folder you see this folder:-
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img14.JPG" /> 
    You need to copy this **adafruit_imageload** , **images**  folder and  **gc9a01.py**  file to the  **CIRCUITPY**  device, as shown in figure
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img12.png" /> 
    You can also display your custom images, for this you need to go "images" folder as shown in below,and save the BMP images of 240x240 
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img16.png" /> 
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img17.png" /> 
    You can online convert any image to BMP image (the size must be 240x240), i a websie below(there are various website)
    https://image.online-convert.com/convert-to-bmp
    
    Finally, you need to run this file **picture_display.py**
    
  * **Display Images From SD Card** -> For display images, I use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). for this first you need to press the boot button then connect the USB, don't release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this file 
    "adafruit-circuitpython- raspberry_pi_pico-en_US-7.1.1.uf2" to this device as shown in figure:
    this is the official website, or yoy can download from here https://circuitpython.org/board/raspberry_pi_pico/
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" /> 
    When you properly insert the circuitpython then you see a new device that looks like the below image:-
    <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />  
    Now, follow all the process of **Display Images**,don't put images to this directory, we use sd card to this. the extra thing you need to do is copy the adafruit_sdcard.py file and paste in this directory, and insert the       BMP images (240x240) in sd card. 
  
  
  * **Memory card reader** -> (use micropython) for round LCD you need to drag and drop the round LCD firmware "firmware.uf2". for this first you need to press the boot button     then connect the USB, don,t release the button until you connect the USB to the laptop. then you see a new device named "RPI-RP2" drag this file "firmware.uf2" to this device   as shown in figure 
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" /> 
  Save the library of SD Card in the pico(file name "sdcard.py")
  Put SD Card in the RoundyPi and run the code(main.py), code read and write the values to the SD Card
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img8.png" /> 
  <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img10.png" /> 
