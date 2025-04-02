import time, asyncio
import Components as com

MAIN_SENSOR_TIME = 0.2
x, y = 0, 0


def initialiseMovement():
    activateMotors()
    activateSensor()

def initialiseSound():
    activateAmplifier()
    activateDecoder()
    activateSpeaker()
    
def moveRandomly():
    pass

async def move():
    while True:
        if not com.Sensor.isThereAnObstacle():
            com.Motor.moveRandomly()
        else:
            com.Motor.steer()
            
        await asyncio.sleep(MAIN_SENSOR_TIME)


def main():
    #pre program pause
    initialiseMovement()
    initialiseSound()
    playMp3()
    asyncio.run(loop())
