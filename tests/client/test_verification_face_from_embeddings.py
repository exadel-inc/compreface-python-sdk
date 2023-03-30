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

from compreface.exceptions.field_exception import IncorrectFieldException
import pytest
import httpretty
import requests
from compreface.config.api_list import RECOGNIZE_EMBEDDINGS_API
from compreface.client import VerificationFaceFromEmbeddingClient
from tests.client.const_config import (
    DOMAIN,
    PORT,
    RECOGNIZE_API_KEY,
    IMAGE_ID,
)


url: str = (
    DOMAIN + ":" + PORT + RECOGNIZE_EMBEDDINGS_API + "/faces/{}/verify".format(IMAGE_ID)
)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    embedding: list = [1, 6, 7, 2]

    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=url,
        json={"embeddings": embedding},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()

    test_subject: VerificationFaceFromEmbeddingClient = (
        VerificationFaceFromEmbeddingClient(RECOGNIZE_API_KEY, DOMAIN, PORT)
    )
    test_response: dict = test_subject.post(embedding, IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_empty_embeddings():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=url,
        json={"embeddings": []},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()

    test_subject: VerificationFaceFromEmbeddingClient = (
        VerificationFaceFromEmbeddingClient(RECOGNIZE_API_KEY, DOMAIN, PORT)
    )
    test_response: dict = test_subject.post(image_id=IMAGE_ID)
    assert response == test_response


def test_post_failed():
    with pytest.raises(IncorrectFieldException):
        test_subject: VerificationFaceFromEmbeddingClient = (
            VerificationFaceFromEmbeddingClient(RECOGNIZE_API_KEY, DOMAIN, PORT)
        )
        test_subject.post()


def test_not_implemented_methods():
    test_subject: VerificationFaceFromEmbeddingClient = (
        VerificationFaceFromEmbeddingClient(RECOGNIZE_API_KEY, DOMAIN, PORT)
    )
    assert test_subject.get() is None
    assert test_subject.put() is None
    assert test_subject.delete() is None
