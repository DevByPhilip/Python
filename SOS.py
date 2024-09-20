from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

def sos():
    # SOS pattern: 3 short, 3 long, 3 short
    for _ in range(3): 
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)
    for _ in range(3): 
        led.value(1)
        time.sleep(0.6)
        led.value(0)
        time.sleep(0.2)
    for _ in range(3):  
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

try:
    while True:
        if not button.value():  
            sos()
            time.sleep(1)  
        else:
            led.value(0) 
except:
    pass

