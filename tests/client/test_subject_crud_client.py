
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
import httpretty
import requests
from compreface.client import SubjectClient
from compreface.config.api_list import SUBJECTS_CRUD_API
from tests.client.const_config import DOMAIN, PORT, DETECTION_API_KEY
"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + SUBJECTS_CRUD_API


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get():
    httpretty.register_uri(
        httpretty.GET,
        url,
        headers={'x-api-key': DETECTION_API_KEY},
        body='{"subjects": ["Subject", "Subject2"]}'
    )
    test_subject: SubjectClient = SubjectClient(DETECTION_API_KEY, DOMAIN, PORT)
    response: dict = requests.get(url=url, headers={'x-api-key': DETECTION_API_KEY}).json()
    test_response: dict = test_subject.get()
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'application/json'},
        body='{"subject": "Subject"}'
    )

    data = {'subject': 'Subject'}

    response: dict = requests.post(
        url=url, data=json.dumps(data), headers={'x-api-key': DETECTION_API_KEY,
                                                 'Content-Type': 'application/json'}).json()

    test_subject: SubjectClient = SubjectClient(DETECTION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post({'subject': 'Subject'})
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_incorrect_response():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'application/json'},
        body='{"subject": "Subjectss"}'
    )

    data = {'subject': 'Subjectss'}

    response: dict = requests.post(
        url=url, data=json.dumps(data), headers={'x-api-key': DETECTION_API_KEY,
                                                 'Content-Type': 'application/json'}).json()

    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'application/json'},
        body='{"subject": "Subject"}'
    )

    test_subject: SubjectClient = SubjectClient(DETECTION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post({'subject': 'Subject'})
    assert response != test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete():
    test_url = url + '/Subject'
    httpretty.register_uri(
        httpretty.DELETE,
        test_url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'application/json'},
        body='{"subject": "Subject"}'
    )

    response: dict = requests.delete(url=test_url,
                                     headers={'x-api-key': DETECTION_API_KEY,
                                              'Content-Type': 'application/json'}).json()

    test_subject: SubjectClient = SubjectClient(DETECTION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.delete("Subject")
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_put():
    test_url = url + '/Subject'
    httpretty.register_uri(
        httpretty.PUT,
        test_url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'application/json'},
        body='{"subject": "NewSubject"}'
    )

    data = {"subject": "NewSubject"}

    response: dict = requests.put(url=test_url, data=json.dumps(data), headers={'x-api-key': DETECTION_API_KEY}).json()

    test_subject: SubjectClient = SubjectClient(DETECTION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.put({"subject": "NewSubject", "api_endpoint": "Subject"})
    assert response == test_response
