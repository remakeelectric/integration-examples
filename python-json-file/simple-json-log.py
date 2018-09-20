#!/usr/bin/env python3
# Karl Palsson <karlp@etactica.com> Sept 2018
__description = """
Simple demonstration of selecting a given variable and saving to a file 
"""

import argparse
import datetime
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Failed to connect, aborting")
        exit(rc)
    client.subscribe("status/local/json/device/%s" % userdata.device)

def on_message(client, userdata, msg):
    js = json.loads(msg.payload)
    if js.get("senml"):
        # Ok, was successful reading
        for e in js["senml"]["e"]:
            if e["n"] == userdata.parameter:
                ds = datetime.datetime.fromtimestamp(js["timestamp_ms"] / 1000)
                print("Found matching parameter: %s %f" % (ds, e["v"]))
                userdata.file.write("%s;%f\n" % (ds, e["v"]))


def domain():
    ap = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__description
    )
    ap.add_argument("--host", "-H", help="MQTT Host name", default="localhost")
    ap.add_argument("--file", "-f", type=argparse.FileType('w'), help="File to save to, will be trampled", required=True)
    ap.add_argument("--device", "-d", help="deviceid to listen to, eg 'E643E5EE2391'", required=True)
    ap.add_argument("--parameter", "-p", help="parameter name to save, eg 'volt/1'", required=True)
    opts = ap.parse_args()

    client = mqtt.Client(userdata=opts)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(opts.host, 1883, 60)
    client.loop_forever()

if __name__  == "__main__":
    domain()