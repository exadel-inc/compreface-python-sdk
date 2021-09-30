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
import json

import requests

from compreface.config.api_list import SUBJECTS_CRUD_API
from ..common import ClientRequest


class SubjectClient(ClientRequest):

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = SUBJECTS_CRUD_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url
        self.headers = {'Content-Type': 'application/json', 'x-api-key': api_key}

    """
        GET request for get all subjects. 

        :return: json with subjects from server.
    """

    def get(self) -> dict:
        url: str = self.url
        result = requests.get(url, headers=self.headers)
        return result.json()

    """
        POST request for add subject without an image. 

        :param subject: fullname

        :return: json with this subject from server.
    """

    def post(self, subject: dict = '') -> dict:
        url: str = self.url
        result = requests.post(url, data=json.dumps(subject), headers=self.headers)
        return result.json()

    """ 
        PUT request to CompreFace server for rename existing subject. 

        :param subject: fullname

        :return: json from server.
    """

    def put(self, request: dict = '') -> dict:
        url: str = self.url + '/' + request.get('api_endpoint')
        result = requests.put(url, data=json.dumps(request), headers=self.headers)
        return result.json()

    """ 
        DELETE request to CompreFace server for delete subjects. 

        :param subject: fullname

        :return: json from server.
    """

    def delete(self, subject: str = '') -> dict:
        url: str = self.url + '/' + subject if subject else self.url
        result = requests.delete(url, headers=self.headers)
        return result.json()
