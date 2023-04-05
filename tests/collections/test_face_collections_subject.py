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
import json
import pytest
import httpretty
import requests


from compreface.config.api_list import SUBJECTS_CRUD_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY

from compreface.collections.face_collections import Subjects

url: str = DOMAIN + ":" + PORT + SUBJECTS_CRUD_API

subject = Subjects(api_key=RECOGNIZE_API_KEY, domain=DOMAIN, port=PORT)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_subject_list():
    httpretty.register_uri(
        httpretty.GET,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1", "Subject2"]',
    )
    response: dict = requests.get(
        url=url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()
    subject_response: dict = subject.list()
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_subject_add():
    subject_added: str = "Subject1"
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1", "Subject2"]',
    )
    response: dict = requests.post(
        url=url,
        data=json.dumps(subject_added),
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()
    subject_response: dict = subject.add(subject_added)
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_subject_update():
    subject_added: str = "Subject1"
    subject_new_name: str = "Subject2"
    update_url: str = url + "/" + subject_added
    httpretty.register_uri(
        httpretty.PUT,
        update_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject2"]',
    )
    response: dict = requests.put(
        url=update_url,
        data=json.dumps(subject_new_name),
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()
    subject_response: dict = subject.update(subject_added, subject_new_name)
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_subject_delete():
    subject_added: str = "Subject1"
    delete_url: str = url + "/" + subject_added
    httpretty.register_uri(
        httpretty.DELETE,
        delete_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1"]',
    )
    response: dict = requests.delete(
        url=delete_url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()
    subject_response: dict = subject.delete(subject_added)
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_subject_delete_all():
    httpretty.register_uri(
        httpretty.DELETE,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1"]',
    )
    response: dict = requests.delete(
        url=url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()
    subject_response: dict = subject.delete_all()
    assert subject_response == response
