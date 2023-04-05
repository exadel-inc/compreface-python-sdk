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

from compreface.common.typed_dict import PredictionCountOptionsDict
import pytest
import httpretty
import requests
from compreface.client.recognize_face_from_embeddings import (
    RecognizeFaceFromEmbeddingClient,
)
from compreface.config.api_list import RECOGNIZE_EMBEDDINGS_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY

"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + RECOGNIZE_EMBEDDINGS_API + "/recognize"


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize():
    embeddings: list = [2, 5, 6]
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=url,
        json={"embeddings": embeddings},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()

    test_subject: RecognizeFaceFromEmbeddingClient = RecognizeFaceFromEmbeddingClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(embeddings)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize_with_options():
    embeddings: list = [2, 5, 6]
    options_url: str = url + "?&prediction_count=1"
    httpretty.register_uri(
        httpretty.POST,
        options_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=options_url,
        json={"embeddings": embeddings},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()

    options: PredictionCountOptionsDict = {"prediction_count": 1}

    test_subject: RecognizeFaceFromEmbeddingClient = RecognizeFaceFromEmbeddingClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(embeddings, options)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize_other_response():
    embeddings: list = [2, 5, 6]
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )
    response: dict = requests.post(
        url=url,
        json={"embeddings": embeddings},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 26, 31 ], "gender" : "female"}]}',
    )
    test_subject: RecognizeFaceFromEmbeddingClient = RecognizeFaceFromEmbeddingClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(embeddings)
    assert response != test_response


def test_not_implemented_methods():
    test_subject: RecognizeFaceFromEmbeddingClient = RecognizeFaceFromEmbeddingClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    assert test_subject.get() is None
    assert test_subject.put() is None
    assert test_subject.delete() is None
