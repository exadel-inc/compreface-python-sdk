# -*- coding: utf-8 -*-

from compreface.config.api_list import RECOGNIZE_CRUD_API
import requests

from ..common import ClientRequest


class DeleteExampleByIdClient(ClientRequest):

    """
        Delete example by id from image_id.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_CRUD_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    """ 
        DELETE request to CompreFace server. Delete example by id from image_id.
        
        :param image_id:
        
        :return: json from server.
    """

    def delete(self, image_id: str = ''):
        url: str = self.url + '/' + image_id
        result = requests.delete(url, headers={'x-api-key': self.api_key})
        return result.json()
