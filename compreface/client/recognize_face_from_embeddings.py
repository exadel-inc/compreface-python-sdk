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

from compreface.common.typed_dict import (
    PredictionCountOptionsDict,
    check_fields_by_name,
)
from compreface.config.api_list import RECOGNIZE_EMBEDDINGS_API
from ..common import ClientRequest


class RecognizeFaceFromEmbeddingClient(ClientRequest):
    """
    The service is used to determine similarities between input embeddings and embeddings within the Face Collection.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_EMBEDDINGS_API
        self.api_key: str = api_key
        self.url: str = domain + ":" + port + self.client_url

    def get(self):
        pass

    """
        POST request for recognize faces in embeddings. 
        
        :param embeddings: An input embeddings. The length depends on the model.
        :param options: dictionary with options for server.
        
        :return: json from server.
    """

    def post(self, embeddings: list = [], options: PredictionCountOptionsDict = {}):
        url: str = self.url + "/recognize?"

        # Validation loop and adding fields to the url.
        for key in options.keys():
            # Checks fields with necessary rules.
            # key - key field by options.
            check_fields_by_name(key, options[key])
            url += "&" + key + "=" + str(options[key])

        # Sending an input source embedding for recognize faces.
        result = requests.post(
            url, json={"embeddings": embeddings}, headers={"x-api-key": self.api_key}
        )
        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
