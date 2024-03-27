from paho.mqtt.client import MQTTMessage
from paho.mqtt.client import Client
from typing import TypedDict


class MessageInfo(TypedDict):
    client: Client
    userdata: dict
    message: MQTTMessage
