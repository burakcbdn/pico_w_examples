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

seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

steps_per_revolution = 200  # Number of steps per revolution of the stepper motor
microsteps = 8  # Number of microsteps per full step
lead_screw_pitch_mm = 2  # Lead screw pitch in millimeters

# Calculate steps per millimeter for each axis
steps_per_mm_x = steps_per_revolution * microsteps / (lead_screw_pitch_mm * 360)
steps_per_mm_y = steps_per_revolution * microsteps / (lead_screw_pitch_mm * 360)
steps_per_mm_z = steps_per_revolution * microsteps / (lead_screw_pitch_mm * 360)

delay = 10

# Function to move the stepper motor one step clockwise
def step_cw(motor):
    for i in range(microsteps):
        for m in range(4):
            motor[m].value(seq[i][m])
        utime.sleep_ms(delay)

# Function to move the stepper motor one step counterclockwise
def step_ccw(motor):
    for i in range(microsteps - 1, -1, -1):
        for m in range(4):
            motor[m].value(seq[i][m])
        utime.sleep_ms(delay)

# Function to move the stepper motor up (Z direction)
def step_up():
    pass

# Function to move the stepper motor down (Z direction)
def step_down():
    pass

# Function to parse G-code and move the stepper motors accordingly
def parse_gcode(gcode):
    commands = gcode.strip().split("\n")
    for command in commands:
        if command.startswith("G1"):
            # Extract X, Y, and Z values from G1 command
            x = float(command.split("X")[1].split(" ")[0])
            y = float(command.split("Y")[1].split(" ")[0])
            z = float(command.split("Z")[1].split(" ")[0])

            # Calculate the number of steps based on the desired movement
            steps_x = int(x * steps_per_mm_x)
            steps_y = int(y * steps_per_mm_y)
            steps_z = int(z * steps_per_mm_z)
            
            print(f"Step x: {steps_x} Step y: {steps_y} Step z: {steps_z}")

            # Move the motors accordingly
            if steps_x > 0:
                for _ in range(steps_x):
                    step_cw(m1)
                    print("stepcw")
            else:
                for _ in range(abs(steps_x)):
                    step_ccw(m1)
                    print("step ccw")

            if steps_y > 0:
                for _ in range(steps_y):
                    step_cw(m2)
            else:
                for _ in range(abs(steps_y)):
                    step_ccw(m2)

            if steps_z > 0:
                for _ in range(steps_z):
                    step_up()
            else:
                for _ in range(abs(steps_z)):
                    step_down()

# Example G-code
gcode = """
G1 X10 Y5 Z2
G1 X-5 Y-8 Z-3
"""

while True:
    parse_gcode(gcode)
    utime.sleep(1)  # Wait for 1 second before parsing the next G-code

