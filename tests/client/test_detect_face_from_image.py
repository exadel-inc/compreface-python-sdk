import os
import httpretty
import requests
from compreface.config.api_list import DETECTION_API
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.client.detect_face_from_image import DetectFaceFromImageClient
from tests.client.const_config import DOMAIN, PORT, DETECTION_API_KEY, FILE_PATH, IMAGE_ID

url: str = DOMAIN + ":" + PORT + DETECTION_API


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': DETECTION_API_KEY}).json()
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT)
    test_response: dict = test_subject.post(FILE_PATH)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_other_response():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}'
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={'file': (name_img, open(FILE_PATH, 'rb'))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={'x-api-key': DETECTION_API_KEY}).json()
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT)
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={'x-api-key': DETECTION_API_KEY,
                 'Content-Type': 'multipart/form-data'},
        body='{"result" : [{"age" : [ 21, 32 ], "gender" : "female"}]}'
    )
    test_response: dict = test_subject.post(FILE_PATH)
    assert response != test_response
