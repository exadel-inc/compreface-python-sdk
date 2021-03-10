# -*- coding: utf-8 -*-

import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from ..common import ClientRequest


class RecognizeFaceFromImageClient(ClientRequest):

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = '/api/v1/faces/recognize'
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    def post(self, image_path: str = '',
             limit: float = 0,
             det_prob_threshold: float = 0,
             prediction_count: int = 0):
        url: str = self.url + '?limit=' + str(limit) + '&prediction_count=' + str(prediction_count) \
                   + '&det_prob_threshold=' + \
                   str(det_prob_threshold)
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
