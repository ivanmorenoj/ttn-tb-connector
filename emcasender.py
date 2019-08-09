import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGSBOARD_HOST = "35.238.206.29"
ACCESS_TOKEN = "vYzJkNhrUqPSeB5lCpz5"

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=5

sensor_data = {'Temperature': 0,'Humidity': 0,'Pressure': 0,'CO': 0,'O3': 0,'SO2': 0,'NO2': 0,'PM1': 0,'PM10': 0,'PM25': 0}

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1882)

client.loop_start()

try:
    while True:
        sensor_data['Temperature']  = random.randint(-60,60)
        sensor_data['Humidity']     = random.randint(0,100) 
        sensor_data['Pressure']     = random.randint(0,100000) 
        sensor_data['CO']           = random.randint(0,10) 
        sensor_data['O3']           = random.randint(0,5) 
        sensor_data['SO2']          = random.randint(0,5) 
        sensor_data['NO2']          = random.randint(0,5) 
        sensor_data['PM1']          = random.randint(0,10) 
        sensor_data['PM10']         = random.randint(0,10) 
        sensor_data['PM25']         = random.randint(0,10) 

        # Sending humidity and temperature data to ThingsBoard
        infot = client.publish("v1/devices/me/telemetry", json.dumps(sensor_data), 1)

        time.sleep(INTERVAL)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()