import dht
import time
from machine import Pin, Timer
from measure_tem_hum import measure
from microdot import Microdot, Response
from net.net import net_connect, blink_connect
from microdot_utemplate import render_template

#CONNECT TO NETWORK
connected = net_connect()

#LED FOR NETWORK STATUS
blink_connect(connected)

#WEB SERVER
app = Microdot()
Response.default_content_type = 'text/html'

@app.route('/', methods=['GET'])
def index(req):
    C,H = measure()
    temperature = C
    humidity = H
    return render_template('index.html', temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run(port=80) 