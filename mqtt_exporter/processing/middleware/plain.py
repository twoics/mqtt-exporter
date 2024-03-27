import json
from json import JSONDecodeError

from mqtt_exporter.processing.middleware.base import InplaceProcessMiddleware, MessageInfo


class PlainTextInplaceProcessMiddleware(InplaceProcessMiddleware):

    def __call__(self, data: MessageInfo) -> None:
        """Converts the payload to json format if it differs from it"""

        message = data['message']
        try:
            json.loads(message.payload)
        except JSONDecodeError:
            message.payload = json.dumps({'msg': message.payload.decode("utf-8")})
