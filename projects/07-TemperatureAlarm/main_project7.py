#Project 7:
#Author: oneaarmdeveloper

import machine
import dht
import time


# Hardware Configuration 
sensor = dht.DHT11(machine.Pin(3))                  
buzzer = machine.Pin(14, machine.Pin.OUT)            


GRENZWERT = 10  


def temperatur_messen():
    """
    Reads current temperature from DHT11 sensor.
    
    Returns:
        float: Temperature in °C
    """
    sensor.measure()
    return sensor.temperature()


def buzzer_alert(times, delay=0.2):
    
    
    for _ in range(times):
        buzzer.value(1)     
        time.sleep(delay)
        buzzer.value(0)     
        time.sleep(delay)


print("Temperaturalarm aktiv.")
print("Schwellenwert: {} °C\n".format(GRENZWERT))

for i in range(5):
    temp = temperatur_messen()
    print("Messung {:02d}/20  →  Temperatur: {} °C".format(i + 1, temp))

    if temp > GRENZWERT:
        print("  ⚠️  ALARM! Temperatur zu hoch!")
        buzzer_alert(3)     

    time.sleep(3)

print("\nMessung abgeschlossen.")