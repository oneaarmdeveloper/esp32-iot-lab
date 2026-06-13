import network
import ntptime
import utime
from time import sleep_ms

try:
    from config import SSID, PASSWD
except ImportError:
    print("ERROR: config.py not found! Please check your files.")
    raise

def connect_wlan(ssid, passwd):
    print(f"Connecting to: {ssid}")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    
    if wlan.isconnected():
        wlan.disconnect()
        sleep_ms(500)
    
    wlan.connect(ssid, passwd)
    
    
    timeout = 0
    while not wlan.isconnected() and timeout < 15:
        sleep_ms(500)
        print(".", end="")
        timeout += 1
    print()
    
    return wlan.isconnected()

def get_local_time():
    print("\n🌍 Fetching time from NTP server...")
    
    
    ntptime.settime()
    sleep_ms(500)
    
    
    utc = utime.localtime()
    
    
    tz_offset = 2
    hour = (utc[3] + tz_offset) % 24
    
    print("✅ Time Synchronized!")
    print(f"Date: {utc[0]}-{utc[1]:02d}-{utc[2]:02d}")
    print(f"Time: {hour:02d}:{utc[4]:02d}:{utc[5]:02d} (UTC+{tz_offset})")

# main
if connect_wlan(SSID, PASSWD):
    get_local_time()
else:
    print(" Connection failed.")