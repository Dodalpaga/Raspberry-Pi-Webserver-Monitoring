from influxdb import InfluxDBClient
from datetime import datetime
import os
import time
import random
import psutil
import bluepy.btle as btle
import struct
import binascii

client = InfluxDBClient(host='localhost', port=8086)
client.drop_database('ACCEL-USAGE-DB')
client.create_database('ACCEL-USAGE-DB')
client.switch_database('ACCEL-USAGE-DB')

#Delegate methods
class ReadDelegate(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        print("Here is the data...")
        print(data)

def convert(characteristic):
    val = binascii.b2a_hex(characteristic.read())
    val = binascii.unhexlify(val)
    val = struct.unpack('f', val)[0]
    return(val)

#Create peripheral, connect, services and write...
p = btle.Peripheral("E9:C9:F5:2F:C7:48", "random")
p.withDelegate(ReadDelegate())

service=p.getServiceByUUID("0000a000-0000-1000-8000-00805f9b34fb")

while(1):
    
    ts = time.time()
    ds = datetime.utcnow()
    
    charact = service.getCharacteristics()[0]
    convert(charact)
        
    AccX = convert(service.getCharacteristics()[0])
    AccY = convert(service.getCharacteristics()[1])
    AccZ = convert(service.getCharacteristics()[2])
    json_body = [
        {
            "measurement": "AcceleroSimulation",
            "time": ds,
            "fields": {
                "AccX": AccX,
                "AccY": AccY,
                "AccZ": AccZ
            }
        }
    ]
    client.write_points(json_body)
