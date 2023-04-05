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

from compreface.config.api_list import VERIFICATION_EMBEDDINGS_API
from compreface.common.client import ClientRequest


class VerifyFaceFromEmbeddingClient(ClientRequest):
    """
    Verify Faces from a Given Image, Embedding.
    """

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = VERIFICATION_EMBEDDINGS_API
        self.api_key: str = api_key
        self.url: str = domain + ":" + port + self.client_url

    def get(self):
        pass

    """
        POST request for compare face between an input source embedding and input target embeddings. 

        
        :param source_embeddings: An input embeddings. The length depends on the model.
        :param targets_embeddings: An array of the target embeddings. The length depends on the model.
        
        :return: json from server.
    """

    def post(self, source_embeddings: list, targets_embeddings: list) -> dict:
        url: str = self.url + "/verify"

        # Sending an input source embedding.
        result = requests.post(
            url,
            json={"source": source_embeddings, "targets": targets_embeddings},
            headers={"x-api-key": self.api_key},
        )

        result.raise_for_status()

        return result.json()

    def put(self):
        pass

    def delete(self):
        pass
