import machine
import utime

# Define the GPIO pins for the stepper motor
coil_A_1_pin = machine.Pin(14, machine.Pin.OUT)
coil_A_2_pin = machine.Pin(15, machine.Pin.OUT)
coil_B_1_pin = machine.Pin(16, machine.Pin.OUT)
coil_B_2_pin = machine.Pin(17, machine.Pin.OUT)

# Define the sequence of steps for the stepper motor
# Each element represents the state of the 4 pins
# in the order A1, A2, B1, B2
seq = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

# Function to move the stepper motor one step clockwise
def step_cw():
    for i in range(4):
        coil_A_1_pin.value(seq[i][0])
        coil_A_2_pin.value(seq[i][1])
        coil_B_1_pin.value(seq[i][2])
        coil_B_2_pin.value(seq[i][3])
        utime.sleep_ms(10)  # Adjust delay as needed for motor speed

# Function to move the stepper motor one step counterclockwise
def step_ccw():
    for i in range(3, -1, -1):
        coil_A_1_pin.value(seq[i][0])
        coil_A_2_pin.value(seq[i][1])
        coil_B_1_pin.value(seq[i][2])
        coil_B_2_pin.value(seq[i][3])
        utime.sleep_ms(10)  # Adjust delay as needed for motor speed

# Example usage:




while True:
    for i in range(64):
        step_ccw()
        utime.sleep(0.05)  # Wait 1 second
    for i in range(64):
        step_cw()
        utime.sleep(0.05)  # Wait 1 second

