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

from compreface.common.multipart_constructor import multipart_constructor
from compreface.common.typed_dict import AllOptionsDict, check_fields_by_name
from compreface.config.api_list import RECOGNIZE_API
from ..common import ClientRequest


class RecognizeFaceFromImageClient(ClientRequest):
    """
        Recognize faces in image. It uses image path for encode and send to CompreFace server.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_API
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self):
        pass

    """
        POST request for recognize faces in image. 
        
        :param image_path: Path to image in file system.
        :param options: dictionary with options for server.
        
        :return: json from server.
    """

    def post(self, image: str = '' or bytes, options: AllOptionsDict = {}):
        url: str = self.url + "?"

        # Validation loop and adding fields to the url.
        for key in options.keys():
            # Checks fields with necessary rules.
            # key - key field by options.
            check_fields_by_name(key, options[key])
            url += '&' + key + "=" + str(options[key])

        # Encoding image from path and encode in multipart for sending to the server.
        m = multipart_constructor(image)

        # Sending encode image for recognize faces.
        result = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                                     'x-api-key': self.api_key})
        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
