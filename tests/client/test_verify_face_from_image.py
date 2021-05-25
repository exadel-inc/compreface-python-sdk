import pytest
import os
import httpretty
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.client import VerifyFaceFromImageClient
from compreface.config.api_list import VERIFICATION_API
from tests.client.const_config import DOMAIN, PORT, VERIFICATION_API_KEY, FILE_PATH
"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + VERIFICATION_API + '/verify'


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': VERIFICATION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'source_image': (name_img, open(
                FILE_PATH, 'rb')), 'target_image': (name_img, open(
                    FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': VERIFICATION_API_KEY, 'Content-Type': m.content_type}).json()
    test_subject: VerifyFaceFromImageClient = VerifyFaceFromImageClient(
        VERIFICATION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(FILE_PATH, FILE_PATH)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_other_response():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': VERIFICATION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'source_image': (name_img, open(
                FILE_PATH, 'rb')), 'target_image': (name_img, open(
                    FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': VERIFICATION_API_KEY, 'Content-Type': m.content_type}).json()
    test_subject: VerifyFaceFromImageClient = VerifyFaceFromImageClient(
        VERIFICATION_API_KEY, DOMAIN, PORT)
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': VERIFICATION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 21, 32 ], "gender" : "female"}]}'
    )
    test_response: dict = test_subject.post(FILE_PATH, FILE_PATH)
    assert response != test_response
