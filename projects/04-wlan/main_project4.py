
import network
from time import sleep_ms

try:
    from config import SSID, PASSWD    
except ImportError:
    print("ERROR: config.py not found! Please create config.py with SSID and PASSWD")
    raise

def connectWLAN(ssid, passwd):
    """
    Connects the ESP32 to a WiFi network.

    Parameters:
        ssid (str):   Network name (your hotspot name)
        passwd (str): Network password (your hotspot password)
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Disconnect from any previous connection
    if wlan.isconnected():
        wlan.disconnect()
        sleep_ms(500)

    print(f"Verbinde mit WLAN: {ssid}...")
    wlan.connect(ssid, passwd)

    
    timeout = 0
    while not wlan.isconnected() and timeout < 20:  
        sleep_ms(500)
        print(".", end="")
        timeout += 1

    print()  
    
    if wlan.isconnected():
        print("\nVerbindung erfolgreich hergestellt")
        print("IP-Adresse:", wlan.ifconfig()[0])
        print("Netzwerkkonfiguration:", wlan.ifconfig())
        return True
    else:
        print("\nVerbindung fehlgeschlagen!")
        print("Bitte überprüfen Sie:")
        print("1. Hotspot auf Pixel 7a ist aktiviert")
        print("2. SSID und PASSWD in config.py sind korrekt")
        print("3. ESP32 ist in Reichweite des Hotspots")
        return False

if SSID == "Ichek":
    print("WARNING: Bitte aktualisieren Sie die SSID in config.py!")
    
connectWLAN(SSID, PASSWD)