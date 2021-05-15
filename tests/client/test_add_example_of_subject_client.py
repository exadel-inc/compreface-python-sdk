import pytest
import os
import httpretty
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.client import AddExampleOfSubjectClient
from compreface.config.api_list import RECOGNIZE_CRUD_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, FILE_PATH
"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get():
    httpretty.register_uri(
        httpretty.GET,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{"faces": [{"image_id": "image_id_subject", "subject": "Subject"}]}'
    )
    test_subject: AddExampleOfSubjectClient = AddExampleOfSubjectClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    response: dict = requests.get(
        url=url, headers={'x-api-key': RECOGNIZE_API_KEY}).json()
    test_response: dict = test_subject.get()
    assert response, test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete():
    httpretty.register_uri(
        httpretty.DELETE,
        url + '?subject=Subject',
        headers={'x-api-key': RECOGNIZE_API_KEY},
        body='{"faces": [{"image_id": "image_id_subject", "subject": "Subject"}]}'
    )
    response: dict = requests.delete(
        url=url, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    test_subject: AddExampleOfSubjectClient = AddExampleOfSubjectClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.delete("Subject")
    assert response, test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():

    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"image_id": "image_id_subject", "subject": "Subject"}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': RECOGNIZE_API_KEY,
                                  'Content-Type': 'multipart/form-data'}).json()

    test_subject: AddExampleOfSubjectClient = AddExampleOfSubjectClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(
        FILE_PATH, "Subject")
    assert response, test_response
