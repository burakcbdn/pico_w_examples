from machine import Pin, PWM

print("Servo test")

import utime

servo = PWM(Pin(12))

servo.freq(50)
while True:
    servo.duty_u16(1350)
    utime.sleep(1)
    servo.duty_u16(8200)
    utime.sleep(1)
