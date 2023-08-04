print("Start Button Test Program")

from machine import Pin
import time

button = Pin(13, Pin.IN, Pin.PULL_UP)


motor1 = Pin(16, Pin.OUT)
motor2 = Pin(17, Pin.OUT)

led_g = Pin(15, Pin.OUT)
led_r = Pin(14, Pin.OUT)

left = False;


button_state = 1
button_last_state = 1

last_press_time = 0

while True:
    button_last_state = button_state
    button_state = button.value()
    if button_state != button_last_state:
        if button_state == 0:
            if left:
                motor1.value(0)
                motor2.value(1)
                led_g.value(1)
                led_r.value(0)
                left = False
            else:
                motor1.value(1)
                motor2.value(0)
                led_g.value(0)
                led_r.value(1)
                left = True
            print("Button Pressed")

            last_press_time = time.ticks_ms()
        else:

            # Check if the button was pressed for more than 1 second
            if time.ticks_diff(time.ticks_ms(), last_press_time) > 1000:
                print("Button Pressed for more than 1 second")
                motor1.value(0)
                motor2.value(0)
                led_g.value(0)
                led_r.value(0)
                left = False
            print("Button Released")

  

    
