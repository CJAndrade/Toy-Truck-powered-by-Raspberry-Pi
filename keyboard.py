#!/usr/bin/env python
# create by @CarmelitoA - add Pi control to the broken Monster toy truck - Feel free to use and remix
# you can run this directly using the shell or add it to Contab
#using the Adafruit DC motor Pi Hat --http://www.adafruit.com/product/2348
import pygame #for more info on keyboard events -- https://www.pygame.org/docs/ref/key.html
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor # follow the learning guide for the setup https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi
import atexit

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
motorBack = mh.getMotor(2) #Back motor of the monster truck connect to terminals 2 on the DC Motor Hat
motorFront = mh.getMotor(3)#Front motor connection
interval = 0.1 #interval to check for key press/release - change to increase/decrease sensetivity
minSpeed = 100 # change this value if you want to reduce the speed of your Truck/Car further. Here 0 will put the motor off.
maxSpeed = 200 # value for Max speed. Here 255 is the Maximum
speed = 100 #Default speed for the back motor

#move foward for 
def moveFoward(speed,runTime):
	motorBack.setSpeed(speed)
	motorBack.run(Adafruit_MotorHAT.FORWARD);
	#time.sleep(runTime);#this is not required as motors are release on key release
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE); #release when key is release
	return;

#moving backward
def moveBackward(speed,runTime):
	motorBack.setSpeed(speed)
	motorBack.run(Adafruit_MotorHAT.BACKWARD);
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	return;

#Turn Right - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnFowardRight(speedBackMotor,speedFrontMotor,runTime):
	motorBack.setSpeed(speedBackMotor)
	motorBack.run(Adafruit_MotorHAT.FORWARD);
	motorFront.setSpeed(speedFrontMotor)
	motorFront.run(Adafruit_MotorHAT.FORWARD);
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEASE);
	return;

#Turn left - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnFowardLeft(speedBackMotor,speedFrontMotor,runTime):
	motorBack.setSpeed(speedBackMotor)
	motorBack.run(Adafruit_MotorHAT.FORWARD);
	motorFront.setSpeed(speedFrontMotor)
	motorFront.run(Adafruit_MotorHAT.BACKWARD);
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEASE);
	return;

#Turn Right - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnBackwardRight(speedBackMotor,speedFrontMotor,runTime):
	motorBack.setSpeed(speedBackMotor)
	motorBack.run(Adafruit_MotorHAT.BACKWARD);
	motorFront.setSpeed(speedFrontMotor)
	motorFront.run(Adafruit_MotorHAT.BACKWARD);
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEASE);
	return;

#Turn left - note this was created for a monster truck toy - which uses a dc motor to move the axel to about 30 degress
def turnBackwardLeft(speedBackMotor,speedFrontMotor,runTime):
	motorBack.setSpeed(speedBackMotor)
	motorBack.run(Adafruit_MotorHAT.BACKWARD);
	motorFront.setSpeed(speedFrontMotor)
	motorFront.run(Adafruit_MotorHAT.FORWARD);
	#time.sleep(runTime);
	# turn on motor
	#motorBack.run(Adafruit_MotorHAT.RELEASE);
	#motorFront.run(Adafruit_MotorHAT.RELEASE);
	return;


pygame.init()
screen = pygame.display.set_mode([400,400]) #this seems to work without a montior connected and also when .py is run via SSH
pygame.display.set_caption("Monster Truck controller")

def funcPygameKey(events):
    # Variables accessible outside this function
    global speed
    global maxSpeed
    global minSpeed
    for event in events:
        if event.type == pygame.QUIT:
        	print 'quite pygame'
        elif event.type == pygame.KEYDOWN:
            # checking if a key is pressed
            if event.key == pygame.K_w: #change the mapping if your not comfotable refer to the url for mapping - https://www.pygame.org/docs/ref/key.html
                print 'Key w -foward pressed'
                print speed
                moveFoward(speed,0.25)
            elif event.key == pygame.K_s:
                print 'Key s -backward pressed'
                moveBackward(speed,0.25)
            elif event.key == pygame.K_a:
                print 'Key a -left turn pressed'
                turnFowardLeft(speed,200,0.25)
            elif event.key == pygame.K_d:
                print 'Key d -right turn pressed'
                turnFowardRight(speed,200,0.25)
            elif event.key == pygame.K_q:
                print 'Key q -increase speed pressed'
                if speed <= maxSpeed:
                	speed = speed + 10 #increaseing speed by 10
                	print 'speed +10'
                else:
                	speed = maxSpeed
                	print 'speed else'
            elif event.key == pygame.K_e:
                print 'Key e - slower speed pressed'
                if speed <= minSpeed:
                	speed = minSpeed
                	print 'speed = minSpeed'
                else:
                	speed = speed - 10
                	print 'speed -10'
            elif event.key == pygame.K_r:
                print 'Key r -back right pressed'
                turnBackwardRight(speed,200,0.25)
            elif event.key == pygame.K_f:
                print 'Key f -back left pressed'
                turnBackwardLeft(speed,200,0.25)
        elif event.type == pygame.KEYUP:
            # checking if a key is released
            if event.key == pygame.K_w:
                print 'Key w-foward released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_s:
                print 'Key s-backward released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_a:
                print 'Key a -left turn released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
                motorFront.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_d:
                print 'Key d -right turn released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
                motorFront.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_q:
                print 'Key q -increase speed released'
            elif event.key == pygame.K_e:
                print 'Key e - slower speed released'
            elif event.key == pygame.K_r:
                print 'Key r -back right released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
                motorFront.run(Adafruit_MotorHAT.RELEASE);
            elif event.key == pygame.K_f:
                print 'Key f -back left released'
                motorBack.run(Adafruit_MotorHAT.RELEASE);
                motorFront.run(Adafruit_MotorHAT.RELEASE);
#moving foward ..
moveFoward(speed,0.25)
time.sleep(0.5);
# turn on motor
motorBack.run(Adafruit_MotorHAT.RELEASE);

try:
	print 'Program running- use your keyboard as a controller'
	while True:
		funcPygameKey(pygame.event.get())

		time.sleep(interval)


except KeyboardInterrupt:

	print 'you choose to exit out of the keyboard controller'
