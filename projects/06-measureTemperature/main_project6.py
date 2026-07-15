#Project 6: DHT11 Temperature sensor
#Author: oneaarmdeveloper
import dht
import machine
import time

# Setup DHT11 on GPIO 4
sensor = dht.DHT11(machine.Pin(3))

def temperatur_messen():
    try:
        sensor.measure()              # Trigger reading
        return sensor.temperature()   # Return temperature
    except OSError:
        print("⚠️ Lesefehler - Bitte Wiring prüfen")
        return None

# Main Program
print("Temperaturmessung gestartet.")
print("Lese 20x alle 3 Sekunden...\n")

for i in range(20):
    temp = temperatur_messen()
    if temp is not None:
        print("Messung {:02d}/20  →  Temperatur: {} °C".format(i + 1, temp))
    time.sleep(3)

print("\nMessung abgeschlossen.")