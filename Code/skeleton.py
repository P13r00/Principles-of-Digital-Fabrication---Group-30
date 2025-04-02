import time, asyncio, pygame
import Components as com

MAIN_SENSOR_TIME = 0.2
AUDIO_PATH = ""
x, y = 0, 0


def initialiseMovement():
    com.Motor.activateMotors()
    com.Sensor.activateSensor()

def initialiseSound():
    com.Amplifier.activateAmplifier()
    com.Decoder.activateDecoder()
    com.Speaker.activateSpeaker()

async def playMp3(): # ASYNC?????????
    # https://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load(AUDIO_PATH)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        #stop when audio is over

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

    #CHECK ASYNCIO FUNCTIONALITY
    asyncio.run(playMp3())
    asyncio.run(loop())

if name == "main":
    main()
