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

import os
import pytest
import httpretty
import requests

from compreface.exceptions.field_exception import IncorrectFieldException
from compreface.common.typed_dict import ExpandedOptionsDict
from compreface.config.api_list import DETECTION_API
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.client.detect_face_from_image import DetectFaceFromImageClient
from tests.client.const_config import (
    DOMAIN,
    PORT,
    DETECTION_API_KEY,
    FILE_PATH,
)

url: str = DOMAIN + ":" + PORT + DETECTION_API


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post():
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
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    test_response: dict = test_subject.post(FILE_PATH)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_with_options():
    options_url: str = (
        url
        + "?&det_prob_threshold=1&limit=1&status=true&face_plugins=calculator,gender"
    )
    httpretty.register_uri(
        httpretty.POST,
        options_url,
        headers={"x-api-key": DETECTION_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={"file": (name_img, open(FILE_PATH, "rb"))}
    )
    response: dict = requests.post(
        url=options_url, data=m, headers={"x-api-key": DETECTION_API_KEY}
    ).json()
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    options: ExpandedOptionsDict = {
        "det_prob_threshold": 1,
        "limit": 1,
        "status": True,
        "face_plugins": "calculator,gender",
    }
    test_response: dict = test_subject.post(FILE_PATH, options)
    assert response == test_response


def test_post_with_options_failed_limit():
    options: ExpandedOptionsDict = {
        "det_prob_threshold": 1,
        "limit": -1,
        "status": True,
        "face_plugins": "calculator",
    }
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    with pytest.raises(IncorrectFieldException):
        test_subject.post(FILE_PATH, options)


def test_post_with_options_failed_det_prob_threshold():
    options: ExpandedOptionsDict = {
        "det_prob_threshold": -1,
        "limit": 1,
        "status": True,
        "face_plugins": "calculator",
    }
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    with pytest.raises(IncorrectFieldException):
        test_subject.post(FILE_PATH, options)


def test_post_with_options_failed_face_plugins():
    options: ExpandedOptionsDict = {
        "det_prob_threshold": 1,
        "limit": 1,
        "status": True,
        "face_plugins": "calculator",
        "size": -1,
    }
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    with pytest.raises(IncorrectFieldException):
        test_subject.post(FILE_PATH, options)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_post_other_response():
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
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": DETECTION_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 21, 32 ], "gender" : "female"}]}',
    )
    test_response: dict = test_subject.post(FILE_PATH)
    assert response != test_response


def test_not_implemented_methods():
    test_subject: DetectFaceFromImageClient = DetectFaceFromImageClient(
        DETECTION_API_KEY, DOMAIN, PORT
    )
    assert test_subject.get() is None
    assert test_subject.put() is None
    assert test_subject.delete() is None
