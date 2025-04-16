import random as rand
import time
import board
import digitalio

class Decoder:
    pass

class Amplifier:
    pass

class Speaker:
    pass

class Sensor:
    trigPin = digitalio.DigitalInOut(board.GP11)
    trigPin.direction = digitalio.Direction.OUTPUT
    
    echoPin = digitalio.DigitalInOut(board.GP12)
    echoPin.direction = digitalio.Direction.INPUT
    
    microS = 0.000001

    def detect_obstacle():
        distance = measure()
        if (distance < 5):
            return (True, distance)
    
    def measure():
        distance = pulse()
        return distance
    
    def pulse():
        trigPin.value = 0
        time.sleep(5 * microS)
        trigPin.value = 1
        time.sleep(10 * microS)
        trigpin.value = 0
        
        return timer()
    
    def timer():
        startTime = time.monotonic()
        finalTime = 0
        while finalTime == 0:
            if echoPin.value == 1:
                finalTime = time.monotonic()
        duration = finalTime - startTime
        cm = (duration/2) / 29.1
        return cm


class Motor:
    def drive(float time):
        

class controller:
    def maxSpeedInTurn(int angle):
        '''calculates the maximum allowable speed in a turn, based on the angle'''
        
    def driveForward(int time):
        '''move forward for time seconds
        stop if detects an obstacle???'''

    def turn(int angle, bool direction)
        '''turn angle degrees either left (false), or right (true)'''
        
    def steer():
        pass
        
    def moveRandomly():
        randTime = rand.randint(0, 5)
        randAngle = rand.randint(0, 360)
        randDirection = bool(rand.getrandbits(1))
        driveForward(randTime)
        turn(randAngle, randDirection)
        
