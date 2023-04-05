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
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.config.api_list import DETECTION_API

from compreface.service.detection_service import DetectionService
from tests.client.const_config import DETECTION_API_KEY, DOMAIN, FILE_PATH, PORT

url: str = DOMAIN + ":" + PORT + DETECTION_API

detection_service = DetectionService(
    api_key=DETECTION_API_KEY, domain=DOMAIN, port=PORT
)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_detect_image():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": DETECTION_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={"file": (name_img, open(FILE_PATH, "rb"))}
    )
    response: dict = requests.post(
        url=url, data=m, headers={"x-api-key": DETECTION_API_KEY}
    ).json()
    subject_response: dict = detection_service.detect(image_path=FILE_PATH)
    assert response == subject_response


def test_get_available_functions_recognition_service():
    assert detection_service.get_available_functions() == []
