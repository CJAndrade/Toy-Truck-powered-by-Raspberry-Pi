This is the code for my neghibours son's Monster toy Truck mod, using a Raspberry Pi  and  Adafruit's DC & Stepper Motor Pi HAT(http://www.adafruit.com/product/2348)

![alt tag](https://github.com/CJAndrade/Toy-Truck-powered-by-Raspberry-Pi/blob/master/ModifiedPartOfTruckPi.jpg)


You have 2 options to control the truck,

1. KeyBoard Controller - if you like playing computer games using your keyboard,which uses pygame to read keypress.
 
    pi@raspberrypi ~ $ python keyboard.py

2. Mobile controller using a flask(http://flask.pocoo.org/) web app.

    pi@raspberrypi ~ $ sudo apt-get install python-pip

    pi@raspberrypi ~ $ sudo pip install flask

    pi@raspberrypi ~/Truck-Pi $ sudo python controller.py

To access the controller flask web app use http://ipaddress-of-Pi:800 



For detailed steps to modify your Monster Truck/Car refer to 
http://www.instructables.com/id/Toy-Truck-Powered-by-Raspberry-Pi/



Unless otherwise stated, this code is released under the CC BY 4.0 license.
