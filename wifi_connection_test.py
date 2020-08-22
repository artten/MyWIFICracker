import pywifi
import comtypes

profile = pywifi.Profile()
profile.ssid = 'KIEV'
profile.auth = pywifi.const.AUTH_ALG_OPEN
profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
profile.key = '0524211522'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)


