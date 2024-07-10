#FUNCTION FOR NETWORK CONNECTION
def net_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SSSD', 'PASSWORD')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    connected = wlan.isconnected()
    return connected
        
        
#FUNCTION FOR LED NETWORK STATUS     
def blink_connect(connected):
    from machine import Pin
    from neopixel import NeoPixel
    import time
    
    led = Pin(2, Pin.OUT)
    np = NeoPixel(led, 1,bpp=3, timing=1)

    RED  = (255, 0, 0)
    BLUE   = (0, 0, 255)
    OFF    = (0, 0, 0)
    
    if connected == True:
        np[0] = BLUE
        np.write()
        time.sleep(5)
        np[0] = OFF
        np.write()
    else:
        np[0] = RED
        np.write()