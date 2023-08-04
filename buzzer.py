import machine
import utime

# Set up the buzzer pin
buzzer_pin = machine.Pin(15)
buzzer = machine.PWM(buzzer_pin)

# Function to control the buzzer
def buzz(frequency, duration):
    buzzer.duty_u16(32768)  # Set duty cycle to 50% (32768/65536)
    buzzer.freq(int(frequency))
    utime.sleep_ms(duration)
    buzzer.duty_u16(0)  # Turn off the buzzer

# Define note frequencies
la3 = 220
si3 = 247
do = 261
re = 294
mi = 329
fa = 349
sol = 392
la = 440
si = 493
do5 = 523

# Play a melody
notes = [la3, do, mi, re, do, mi, la3, do, mi, re, do, si3]

durations = [200,200,200,500,200,1200, 200,200,200,500,200,700,]

for duration, note in zip(durations, notes):
    buzz(note, duration)
    utime.sleep_ms(100)

