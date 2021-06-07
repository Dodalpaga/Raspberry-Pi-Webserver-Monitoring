from influxdb import InfluxDBClient
from datetime import datetime
import os
import speedtest 
import time
import random
import psutil

client = InfluxDBClient(host='localhost', port=8086)
client.drop_database('NETWORK-USAGE-DB')
client.create_database('NETWORK-USAGE-DB')
client.switch_database('NETWORK-USAGE-DB')
while(1):
    ts = time.time()
    ds = datetime.utcnow()
    
    st = speedtest.Speedtest()
    servernames =[]
    st.get_servers(servernames)
    
    DownloadRate = (st.download()/1000000)
    UploadRate = (st.upload()/1000000)
    Ping = (st.results.ping)
    
    json_body = [
        {
            "measurement": "Speedtest",
            "time": ds,
            "fields": {
                "DownloadRate": DownloadRate,
                "UploadRate": UploadRate,
                "Ping": Ping
            }
        }
    ]
    client.write_points(json_body)

