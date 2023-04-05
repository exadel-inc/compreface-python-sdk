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
from compreface.client.delete_example_by_id import DeleteExampleByIdClient
from compreface.config.api_list import RECOGNIZE_CRUD_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, IMAGE_ID

url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + "/" + IMAGE_ID


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.delete(
        url=url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_other_response():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.delete(
        url=url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    httpretty.register_uri(
        httpretty.DELETE, url, headers={"x-api-key": RECOGNIZE_API_KEY}, body="{}"
    )
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response != test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_empty():
    empty_url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + "/"
    httpretty.register_uri(
        httpretty.DELETE,
        empty_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.delete(
        url=empty_url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    httpretty.register_uri(
        httpretty.DELETE, url, headers={"x-api-key": RECOGNIZE_API_KEY}, body="{}"
    )
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response != test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_multiple_delete():
    url_delete: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + "/delete"
    image_ids: list = ["1", "2", "3"]
    httpretty.register_uri(
        httpretty.POST,
        url_delete,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.post(
        url=url_delete, json=image_ids, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(image_ids)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_multiple_delete_empty():
    url_delete: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + "/delete"
    httpretty.register_uri(
        httpretty.POST,
        url_delete,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.post(
        url=url_delete, json=[], headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post()
    assert response == test_response


def test_not_implemented_methods():
    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT
    )
    assert test_subject.get() is None
    assert test_subject.put() is None
