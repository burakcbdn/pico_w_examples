
import machine
import utime

# Define the GPIO pins for the stepper motor
m1_1 = machine.Pin(2, machine.Pin.OUT)
m1_2 = machine.Pin(3, machine.Pin.OUT)
m1_3 = machine.Pin(4, machine.Pin.OUT)
m1_4 = machine.Pin(5, machine.Pin.OUT)

m2_1 = machine.Pin(18, machine.Pin.OUT)
m2_2 = machine.Pin(19, machine.Pin.OUT)
m2_3 = machine.Pin(20, machine.Pin.OUT)
m2_4 = machine.Pin(21, machine.Pin.OUT)

m1 = [m1_1, m1_2, m1_3, m1_4]
m2 = [m2_1, m2_2, m2_3, m2_4]

# Define the sequence of steps for the stepper motor
# Each element represents the state of the 4 pins
# in the order A1, A2, B1, B2
seq = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

delay = 10

# Function to move the stepper motor one step clockwise
def step_cw(motor):
    for i in range(4):
        for m in range(4):
            motor[m].value(seq[i][m])
            utime.sleep_ms(delay)  # Adjust delay as needed for motor speed

# Function to move the stepper motor one step counterclockwise
def step_ccw(motor):
    for i in range(3, -1, -1):
        for m in range(4):
            motor[m].value(seq[i][m])
            utime.sleep_ms(delay)
       

# Example usage:


while True:
    for i in range(20):
        step_ccw(m1)
        step_ccw(m2)
        utime.sleep(0.05)  # Wait 1 second
    for i in range(20):
        step_cw(m1)
        step_cw(m2)
        utime.sleep(0.05)  # Wait 1 second


