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

import pytest
import httpretty
import requests
from compreface.client import VerifyFaceFromEmbeddingClient
from compreface.config.api_list import VERIFICATION_EMBEDDINGS_API
from tests.client.const_config import DOMAIN, PORT, VERIFICATION_API_KEY

"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + VERIFICATION_EMBEDDINGS_API + "/verify"


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    source_embeddings: list = [1, 3, 4]
    targets_embeddings: list = [2, 5, 6]
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={
            "x-api-key": VERIFICATION_API_KEY,
        },
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=url,
        json={"targets": source_embeddings, "source": targets_embeddings},
        headers={"x-api-key": VERIFICATION_API_KEY},
    ).json()
    test_subject: VerifyFaceFromEmbeddingClient = VerifyFaceFromEmbeddingClient(
        VERIFICATION_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(source_embeddings, targets_embeddings)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_other_response():
    source_embeddings: list = [1, 3, 4]
    targets_embeddings: list = [2, 5, 6]
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={
            "x-api-key": VERIFICATION_API_KEY,
        },
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=url,
        json={"targets": source_embeddings, "source": targets_embeddings},
        headers={"x-api-key": VERIFICATION_API_KEY},
    ).json()
    test_subject: VerifyFaceFromEmbeddingClient = VerifyFaceFromEmbeddingClient(
        VERIFICATION_API_KEY, DOMAIN, PORT
    )
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={
            "x-api-key": VERIFICATION_API_KEY,
        },
        body='{"result" : [{"age" : [ 21, 32 ], "gender" : "female"}]}',
    )
    test_response: dict = test_subject.post(source_embeddings, targets_embeddings)
    assert response != test_response


def test_not_implemented_methods():
    test_subject: VerifyFaceFromEmbeddingClient = VerifyFaceFromEmbeddingClient(
        VERIFICATION_API_KEY, DOMAIN, PORT
    )
    assert test_subject.get() is None
    assert test_subject.put() is None
    assert test_subject.delete() is None
