import time
import board
import digitalio
import pwmio

MAX_DISTANCE = 15

# --- Ultrasonic Sensor Pins ---
trigPin = digitalio.DigitalInOut(board.GP11)
trigPin.direction = digitalio.Direction.OUTPUT

echoPin = digitalio.DigitalInOut(board.GP12)
echoPin.direction = digitalio.Direction.INPUT

microS = 0.000001

# --- Motor Direction Pins ---
in1 = digitalio.DigitalInOut(board.GP0)
in1.direction = digitalio.Direction.OUTPUT

in2 = digitalio.DigitalInOut(board.GP1)
in2.direction = digitalio.Direction.OUTPUT

in3 = digitalio.DigitalInOut(board.GP3)
in3.direction = digitalio.Direction.OUTPUT

in4 = digitalio.DigitalInOut(board.GP4)
in4.direction = digitalio.Direction.OUTPUT

# --- Motor Speed Control (PWM) ---
ena1 = pwmio.PWMOut(board.GP2, frequency=1000)
ena2 = pwmio.PWMOut(board.GP5, frequency=1000)

# --- Optional Switch Input ---
switch = digitalio.DigitalInOut(board.GP6)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

# --- Motor Control Functions ---
def motors_on():
    in1.value = True
    in2.value = False
    in3.value = False
    in4.value = True
    ena1.duty_cycle = 65535
    ena2.duty_cycle = 65535
    print("Motors ON")

def motors_off():
    ena1.duty_cycle = 0
    ena2.duty_cycle = 0
    in1.value = False
    in2.value = False
    in3.value = False
    in4.value = False
    print("Motors OFF")

# --- Distance Measurement ---
def measure_distance_cm():
    trigPin.value = False
    time.sleep(5 * microS)
    trigPin.value = True
    time.sleep(10 * microS)
    trigPin.value = False

    while echoPin.value == 0:
        pass
    start = time.monotonic()

    while echoPin.value == 1:
        pass
    end = time.monotonic()

    duration = end - start
    distance = (duration * 1000000) / 58.2  # Convert to cm
    return distance

# --- Main Loop ---
try:
    while True:
        distance = measure_distance_cm()
        print(f"Distance: {distance:.2f} cm")

        # You can adjust this threshold
        if switch.value == True:  # Optional: only move if switch not pressed
            if distance < MAX_DISTANCE:
                motors_off()
            else:
                motors_on()
        else:
            motors_off()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Interrupted. Stopping motors...")
    motors_off()
