# -*- coding: utf-8 -*-

from compreface.config.api_list import RECOGNIZE_CRUD_API
import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from ..common import ClientRequest


class VerifyFaceFromImageClient(ClientRequest):
    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_CRUD_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    def post(self,
             image_path: str = '',
             image_id: str = ''):
        url: str = self.url + '/' + image_id + '/verify'
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
