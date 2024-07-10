import time
from machine import Timer

#FUNCTION FOR TEMPERATURE AND HUMITIDY
def measure():
    import dht
    from machine import Pin, Timer
    
    dht22 = dht.DHT22(Pin(4))
    
    dht22.measure()
    temp_var = str(dht22.temperature()) + "C"
    hum_var  = str(dht22.humidity()) + "%"
    return temp_var, hum_var