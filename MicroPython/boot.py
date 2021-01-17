# Boot
import network
sat_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connexion au réseau ...')
    sta_if.active(True)
    sta_if.connect('Galaxy A10s1304', 'Junior@976')
    while not sta_if.isconnected():
        pass
print('configuration réseau:', stat_if.ifconfig())

    
