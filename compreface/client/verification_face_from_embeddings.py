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

from compreface.config.api_list import RECOGNIZE_EMBEDDINGS_API
from compreface.exceptions.field_exception import IncorrectFieldException
from ..common import ClientRequest


class VerificationFaceFromEmbeddingClient(ClientRequest):
    """
    Face Verification Service, Embedding.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = RECOGNIZE_EMBEDDINGS_API
        self.api_key: str = api_key
        self.url: str = domain + ":" + port + self.client_url

    def get(self):
        pass

    """
        POST the endpoint is used to compare input embeddings to the embedding stored in Face Collection. 
        
        :param image_id: an id of the source embedding within the Face Collection.
        :param embeddings: an input embeddings. The length depends on the model.
        
        :return: json from server.
    """

    def post(self, embeddings: list = [], image_id: str = "") -> dict:
        if image_id is None or image_id == "":
            raise IncorrectFieldException("image_id should be not empty.")

        url: str = self.url + "/faces/{}/verify".format(image_id)

        # Sending input source embedding and input target embeddings.
        result = requests.post(
            url, json={"embeddings": embeddings}, headers={"x-api-key": self.api_key}
        )
        result.raise_for_status()

        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
