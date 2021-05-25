import os
import httpretty
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.config.api_list import RECOGNIZE_CRUD_API
from compreface.client import CompareFaceFromImageClient
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, FILE_PATH, IMAGE_ID

url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API + '/' + IMAGE_ID + '/verify'


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    test_subject: CompareFaceFromImageClient = CompareFaceFromImageClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(FILE_PATH, IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_other_response():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': RECOGNIZE_API_KEY}).json()

    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 26, 31 ], "gender" : "female"}]}'
    )
    test_subject: CompareFaceFromImageClient = CompareFaceFromImageClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(FILE_PATH, IMAGE_ID)
    assert response != test_response
