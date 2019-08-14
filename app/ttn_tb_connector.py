import time
import ttn
import json
import paho.mqtt.client as tbmqtt


with open('config/config.json') as config_file:
    data_cfg = json.load(config_file)
    
TTN_APP_ID      = data_cfg['ttn']['app_id']
TTN_ACCESS_KEY  = data_cfg['ttn']['access_key']

TB_HOST         = data_cfg['tb']['host']
TB_ACCESS_TOKEN = data_cfg['tb']['token']
TB_PORT         = data_cfg['tb']['port']

DELAY_TIME      = data_cfg['delay']

print("Wait to init for",DELAY_TIME, "secconds")
try:
    for i in range(DELAY_TIME):
        time.sleep(1)
except KeyboardInterrupt:
    pass

tb_client = tbmqtt.Client()

# Set access token
tb_client.username_pw_set(TB_ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
tb_client.connect(TB_HOST, TB_PORT)

tb_client.loop_start()

def uplink_raw_callback(msg, client):
    j_msg = json.loads(msg.payload.decode("utf-8"))
    info = tb_client.publish("v1/devices/me/telemetry", json.dumps(j_msg['payload_fields']), 1)
    info.wait_for_publish()

handler = ttn.HandlerClient(TTN_APP_ID, TTN_ACCESS_KEY)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_raw_callback(uplink_raw_callback)
mqtt_client.connect()

print("Init connector")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass

mqtt_client.close()
