# create by @CarmelitoA  - to repair/add Pi control to the broken moster truck - Feel free to use and remix
# you can run this directly using the shell
#using the Adafruit DC motor Pi Hat http://www.adafruit.com/product/2348
import pygame #for more info on keyboard events https://www.pygame.org/docs/ref/key.html
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor # follow the learning guide for the setup https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi
import atexit
#importing flask 
from flask import Flask,request, redirect,render_template
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60) #CJA -Modified from 0X61
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)
#motor pin setup on the Adafruit DC motor Pi Hat
motorBack = mh.getMotor(2)
motorFront = mh.getMotor(3)
interval = 1 #interval to check for key press/release - change to increase/decrease sensetivity
minSpeed = 100
maxSpeed = 200
speed = 100 #intal speed 

#move foward for 
def moveFoward(speed,runTime):
    motorBack.setSpeed(speed)
    motorBack.run(Adafruit_MotorHAT.FORWARD);
    time.sleep(runTime);#this is not required as motors are release on key release
    #turn on motor
    motorBack.run(Adafruit_MotorHAT.RELEASE); #release when key is release
    return;
#moving backward
def moveBackward(speed,runTime):
    motorBack.setSpeed(speed)
    motorBack.run(Adafruit_MotorHAT.BACKWARD);
    time.sleep(runTime);
    # turn on motor
    motorBack.run(Adafruit_MotorHAT.RELEASE);
    return;
#Turn Right - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnFowardRight(speedBackMotor,speedFrontMotor,runTime):
    motorBack.setSpeed(speedBackMotor)
    motorBack.run(Adafruit_MotorHAT.FORWARD);
    motorFront.setSpeed(speedFrontMotor)
    motorFront.run(Adafruit_MotorHAT.FORWARD);
    time.sleep(runTime);
    # turn on motor
    motorBack.run(Adafruit_MotorHAT.RELEASE);
    motorFront.run(Adafruit_MotorHAT.RELEASE);
    return;

#Turn left - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnFowardLeft(speedBackMotor,speedFrontMotor,runTime):
    motorBack.setSpeed(speedBackMotor)
    motorBack.run(Adafruit_MotorHAT.FORWARD);
    motorFront.setSpeed(speedFrontMotor)
    motorFront.run(Adafruit_MotorHAT.BACKWARD);
    time.sleep(runTime);
    # turn on motor
    motorBack.run(Adafruit_MotorHAT.RELEASE);
    motorFront.run(Adafruit_MotorHAT.RELEASE);
    return;

#Increase speed 
def increaseSpeed():
    global speed
    global maxSpeed
    global minSpeed
    if speed <= maxSpeed:
        speed = speed + 10 #increaseing speed by 10
        print 'speed +10'
    else:
        speed = maxSpeed

#Decrease speed
def decreaseSpeed():
    global speed
    global maxSpeed
    global minSpeed
    if speed <= minSpeed:
        speed = minSpeed
        print 'speed = minSpeed'
    else:
        speed = speed - 10
        print 'speed -10'



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/controlit', methods = ['POST'])
def signup():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Fast':
        increaseSpeed()
    elif buttonHit == 'Slow':
        decreaseSpeed()
    elif buttonHit == 'Foward':
        moveFoward(speed,2) #increase or decrese this time for sensitivity
	print ("Move Foward")
    elif buttonHit == 'Back':
        moveBackward(speed,2)
	print ("Move Back")
    elif buttonHit == 'Left':
        turnFowardLeft(speed,220,2)
	print ("Move Left")
    elif buttonHit == 'Right':
        turnFowardRight(speed,220,2)
	print ("Move Right")
    else :
        print("Do Nothing")
    
		
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=800 ,debug = True)
