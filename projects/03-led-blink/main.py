from machine import Pin
from time import sleep


led_rot = Pin(2, Pin.OUT)

print("Red LED will blink 5 times...")

# Blink loop
for i in range(5):
    led_rot.on()   
    sleep(0.5)     
    led_rot.off()  
    sleep(0.5)     

print("Done!")