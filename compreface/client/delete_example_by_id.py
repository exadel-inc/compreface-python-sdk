"""
    Copyright(c) 2021 the original author or authors

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https: // www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the License for the specific language governing
    permissions and limitations under the License.
 """

import requests

from compreface.config.api_list import RECOGNIZE_CRUD_API
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
