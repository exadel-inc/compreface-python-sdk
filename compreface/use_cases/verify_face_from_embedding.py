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

from compreface.client.verify_face_from_embeddings import VerifyFaceFromEmbeddingClient
from dataclasses import dataclass


class VerifyFaceFromEmbedding:
    @dataclass
    class Request:
        api_key: str
        targets_embeddings: list
        source_embeddings: list

    def __init__(self, domain: str, port: str, api_key: str):
        self.verify_face_from_embedding = VerifyFaceFromEmbeddingClient(
            api_key=api_key, domain=domain, port=port
        )

    def execute(self, request: Request):
        result: dict = self.verify_face_from_embedding.post(
            request.source_embeddings,
            request.targets_embeddings,
        )
        return result
