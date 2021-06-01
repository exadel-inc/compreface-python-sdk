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

url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + '/' + IMAGE_ID


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}'
    )
    response: dict = requests.delete(
        url=url, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_other_response():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}'
    )
    response: dict = requests.delete(
        url=url, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    test_subject: DeleteExampleByIdClient = DeleteExampleByIdClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{}'
    )
    test_response: dict = test_subject.delete(IMAGE_ID)
    assert response != test_response
