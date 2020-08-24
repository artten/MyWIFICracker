import pywifi
import time
# import comtypes


def connect(ssid, password):
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = password

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    profile = iface.add_network_profile(profile)
    iface.connect(profile)

def disconnect():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()


