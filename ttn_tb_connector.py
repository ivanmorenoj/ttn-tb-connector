import time
import ttn
import json
import paho.mqtt.client as tbmqtt

TTN_APP_ID = "emca"
TTN_ACCESS_KEY = "ttn-account-v2.Ebyo38DrTI5dynOb28aw0ExjDLYZGGsr4D6yanc9jcs"

TB_HOST = "127.0.0.1"
TB_ACCESS_TOKEN = "vYzJkNhrUqPSeB5lCpz5"
TB_PORT = 1882

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

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    pass

mqtt_client.close()
