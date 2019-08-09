import time
import ttn
import json

TTN_APP_ID = "emca"
TTN_ACCESS_KEY = "ttn-account-v2.Ebyo38DrTI5dynOb28aw0ExjDLYZGGsr4D6yanc9jcs"

def uplink_raw_callback(msg, client):
    j_msg = json.loads(msg.payload.decode("utf-8"))
    print(j_msg['payload_fields'])

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
