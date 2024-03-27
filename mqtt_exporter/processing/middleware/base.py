from typing import Protocol

from mqtt_exporter.processing.dto import MessageInfo


class InplaceProcessMiddleware(Protocol):

    def __call__(self, data: MessageInfo) -> None:
        """
        Preprocessing input data from MQTT.
        The middleware changes the parameters of the passed object based on its tasks
        """
