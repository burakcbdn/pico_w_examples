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
def step_cw(motor, steps):
    for _ in range(steps):
        for i in range(4):
            for m in range(4):
                motor[m].value(seq[i][m])
                utime.sleep_ms(delay)  # Adjust delay as needed for motor speed

# Function to move the stepper motor one step counterclockwise
def step_ccw(motor, steps):
    for _ in range(steps):
        for i in range(3, -1, -1):
            for m in range(4):
                motor[m].value(seq[i][m])
                utime.sleep_ms(delay)

# Function to move up (Z-axis)
def move_up(distance):
    # Implement your code to move the Z-axis up here
    pass

# Function to move down (Z-axis)
def move_down(distance):
    # Implement your code to move the Z-axis down here
    pass

# Function to move the X-axis
def move_x(distance):
    steps = int(distance * steps_per_mm_x)
    print(steps)
    if steps > 0:
        step_cw(m1, steps)
    else:
        step_ccw(m1, abs(steps))

# Function to move the Y-axis
def move_y(distance):
    steps = int(distance * steps_per_mm_y)
    print(steps)
    if steps > 0:
        step_cw(m2, steps)
    else:
        step_ccw(m2, abs(steps))

# Function to parse G-code commands
def parse_gcode(gcode):
    command = gcode.split()[0]  # Get the command (e.g., G0, G1)
    if command == 'G0' or command == 'G1':
        params = gcode.split()[1:]  # Get the parameters of the command
        for param in params:
            if param[0] == 'X':  # Move X-axis
                distance = float(param[1:])
                move_x(distance)
            elif param[0] == 'Y':  # Move Y-axis
                distance = float(param[1:])
                move_y(distance)
            elif param[0] == 'Z':  # Move Z-axis
                distance = float(param[1:])
                if distance > 0:
                    move_up(distance)
                else:
                    move_down(abs(distance))

# Example usage:
gcode_commands = [
    'G0 X10 Y20',   # Move rapidly to X=10, Y=20
    'G1 X30 Y40',   # Move linearly to X=30, Y=40
    'G0 Z5',        # Move Z-axis up by 5 units
    'G1 Z-3.5',     # Move Z-axis down by 3.5 units
]

steps_per_rev = 5
# Define the steps per millimeter for X and Y axes
steps_per_mm_x = 1.5 / steps_per_rev
steps_per_mm_y = steps_per_mm_x

for gcode in gcode_commands:
    parse_gcode(gcode)
    utime.sleep(0.5)  # Wait for motors to stop (adjust delay if needed)


