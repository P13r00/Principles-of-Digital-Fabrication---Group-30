import random as rand

class Decoder:
    pass

class Amplifier:
    pass

class Speaker:
    pass

class Sensor:
    def isThereAnObstacle():
        pass

class Motor:
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
        
