import time
import board
import digitalio

trigPin = digitalio.DigitalInOut(board.GP11)
trigPin.direction = digitalio.Direction.OUTPUT

echoPin = digitalio.DigitalInOut(board.GP12)
echoPin.direction = digitalio.Direction.INPUT

microS = 0.000001

def main():
    while True:
        distance = measure()
        print(distance + " cm")
        time.sleep(0.5)

def measure():
    return pulse()

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
