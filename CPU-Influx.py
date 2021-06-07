from influxdb import InfluxDBClient
from datetime import datetime
import os
import time
import random
import psutil

client = InfluxDBClient(host='localhost', port=8086)
client.drop_database('CPU-USAGE-DB')
client.create_database('CPU-USAGE-DB')
client.switch_database('CPU-USAGE-DB')
while(1):
    ts = time.time()
    ds = datetime.utcnow()
    AccX = random.uniform(0.95,1.05)
    AccY = random.uniform(0,0.08)
    AccZ = random.uniform(0,0.06)
    RAM = psutil.virtual_memory().percent
    CPU = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]
    DISK = psutil.disk_usage('/')[3]
    json_body = [
        {
            "measurement": "AcceleroSimulation",
            "time": ds,
            "fields": {
                "AccX": AccX,
                "AccY": AccY,
                "AccZ": AccZ
            }
        },
        {
            "measurement": "CPU",
            "time": ds,
            "fields": {
                "DISK": DISK,
                "CPU" : CPU,
                "RAM": RAM
            }
        }
    ]
    print(ds)
    print(str(AccX) + " " + str(AccY) + " " + str(AccZ))
    client.write_points(json_body)
    time.sleep(0.2)
