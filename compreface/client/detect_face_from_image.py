import os
import requests
from ..common import ClientRequest
from compreface.config.api_list import DETECTION_API
from requests_toolbelt.multipart.encoder import MultipartEncoder


class DetectFaceFromImageClient(ClientRequest):
    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = DETECTION_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    def post(self, image_path: str = ''):
        url: str = self.url
        name_img: str = os.path.basename(image_path)
        m = MultipartEncoder(
            fields={'file': (name_img, open(image_path, 'rb'))}
        )
        result = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                                     'x-api-key': self.api_key})
        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
