import os
import pytest
import httpretty
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.client.recognize_face_from_image import RecognizeFaceFromImageClient
from compreface.config.api_list import RECOGNIZE_API
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, FILE_PATH
"""
    Server configuration
"""
url: str = DOMAIN + ":" + PORT + RECOGNIZE_API


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': RECOGNIZE_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )
    name_img: str = os.path.basename(FILE_PATH)
    m = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': RECOGNIZE_API_KEY, 'Content-Type': 'multipart/form-data'}).json()

    test_subject: RecognizeFaceFromImageClient = RecognizeFaceFromImageClient(
        RECOGNIZE_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(FILE_PATH)
    assert response, test_response
