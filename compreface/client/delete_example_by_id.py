# -*- coding: utf-8 -*-

import requests

from ..common import ClientRequest


class DeleteExampleByIdClient(ClientRequest):

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = '/api/v1/faces/'
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self, image_id: str = ''):
        url: str = self.url + image_id
        result = requests.delete(url, headers={'x-api-key': self.api_key})
        return result.json()
