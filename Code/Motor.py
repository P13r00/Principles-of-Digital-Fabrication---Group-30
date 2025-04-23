import time
import board
import digitalio
import pwmio

# Motor direction pins
in1 = digitalio.DigitalInOut(board.GP0)
in1.direction = digitalio.Direction.OUTPUT

in2 = digitalio.DigitalInOut(board.GP1)
in2.direction = digitalio.Direction.OUTPUT

in3 = digitalio.DigitalInOut(board.GP3)
in3.direction = digitalio.Direction.OUTPUT

in4 = digitalio.DigitalInOut(board.GP4)
in4.direction = digitalio.Direction.OUTPUT

# Motor speed control (PWM)
ena1 = pwmio.PWMOut(board.GP2, frequency=1000)
ena2 = pwmio.PWMOut(board.GP5, frequency=1000)

# Switch input pin
switch = digitalio.DigitalInOut(board.GP6)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN  # Pull-down resistor

def motors_on():
    in1.value = True
    in2.value = False
    in3.value = False
    in4.value = True
    ena1.duty_cycle = 65535  # Full speed
    ena2.duty_cycle = 65535  # Full speed

    print("Motors should be running")

def motors_off():
    ena1.duty_cycle = 0  # Stop motor 1
    ena2.duty_cycle = 0  # Stop motor 2
    in1.value = False
    in2.value = False
    in3.value = False
    in4.value = False
    print("Motors stopped")

motors_on()
try:
    while True:
        print("Switch State: ", switch.value)  # Print switch state for debugging

        if not switch.value:  # Switch is pressed (GP6 pulled HIGH by switch)
            motors_on()
        else:
            motors_off()

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted. Cleaning up...")
    motors_off()  # Ensure motors stop on exit
