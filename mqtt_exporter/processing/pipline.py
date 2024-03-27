from typing import List

from paho.mqtt.client import MQTTMessage
from paho.mqtt.client import Client

from mqtt_exporter.processing.dto import MessageInfo
from mqtt_exporter.processing.middleware.base import InplaceProcessMiddleware


class MiddlewarePipeline:

    def __init__(self, middlewares: List[InplaceProcessMiddleware]):
        self._middlewares = middlewares

    def process(self, client: Client, userdata: dict, msg: MQTTMessage) -> None:
        """Based on specified middleware, preprocesses input messages from MQTT in place"""

        data = MessageInfo(client=client, userdata=userdata, message=msg)
        for inplace_middleware in self._middlewares:
            inplace_middleware(data)
