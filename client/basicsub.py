#!/usr/bin/env python3

import signal
import sys
import json
import argparse
import paho.mqtt.client as mqtt

parser = argparse.ArgumentParser(description='Send silly messages to an MQTT server')

parser.add_argument('--server', type=str, 
                    default="localhost",
                    help='The MQTT server hostname')

parser.add_argument('--port', type=int,
                    default=1883,
                    help='The server port')

parser.add_argument('--message', type=str,
                    help='A JSON string')

args = parser.parse_args()

client = mqtt.Client()


def signal_handler(sig, frame):
    print("Disconnecting")
    client.disconnect()
    sys.exit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("debug")


def on_message(client, userdata, msg):
    print(f"{msg.topic} - {str(msg.payload)}")


client.on_connect = on_connect
client.on_message = on_message

client.connect(args.server, args.port, 60)

signal.signal(signal.SIGINT, signal_handler)

client.loop_forever()
