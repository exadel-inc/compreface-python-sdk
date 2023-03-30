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
import requests
import httpretty
import os
from requests_toolbelt.multipart.encoder import MultipartEncoder
from compreface.config.api_list import (
    DETECTION_API,
    RECOGNIZE_EMBEDDINGS_API,
    VERIFICATION_EMBEDDINGS_API,
)

from compreface.core.model import CompreFace
from tests.client.const_config import (
    DETECTION_API_KEY,
    RECOGNIZE_API_KEY,
    DOMAIN,
    FILE_PATH,
    PORT,
    VERIFICATION_API_KEY,
)

compreface = CompreFace(port="", domain="")
compreface.options = {}
compreface.port = PORT
compreface.domain = DOMAIN


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_init_face_recognition_compreface():
    recognition_service = compreface.init_face_recognition(RECOGNIZE_API_KEY)
    embeddings: list = [2, 5, 6]
    embeddings_url: str = (
        compreface.domain
        + ":"
        + compreface.port
        + RECOGNIZE_EMBEDDINGS_API
        + "/recognize"
    )
    httpretty.register_uri(
        httpretty.POST,
        embeddings_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=embeddings_url,
        json={"embeddings": embeddings},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()

    assert response == recognition_service.recognize_embedding(
        embeddings, compreface.options
    )


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_init_face_verification_compreface():
    verification_service = compreface.init_face_verification(VERIFICATION_API_KEY)
    embeddings_url: str = (
        compreface.domain
        + ":"
        + compreface.port
        + VERIFICATION_EMBEDDINGS_API
        + "/verify"
    )
    source_embeddings: list = [1, 3, 4]
    targets_embeddings: list = [2, 5, 6]
    httpretty.register_uri(
        httpretty.POST,
        embeddings_url,
        headers={
            "x-api-key": VERIFICATION_API_KEY,
        },
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=embeddings_url,
        json={"targets": source_embeddings, "source": targets_embeddings},
        headers={"x-api-key": VERIFICATION_API_KEY},
    ).json()
    subject_response: dict = verification_service.verify_embedding(
        source_embeddings, targets_embeddings
    )
    assert response == subject_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_init_face_detection_compreface():
    detection_service = compreface.init_face_detection(VERIFICATION_API_KEY)
    detection_url = compreface.domain + ":" + compreface.port + DETECTION_API
    httpretty.register_uri(
        httpretty.POST,
        detection_url,
        headers={"x-api-key": DETECTION_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={"file": (name_img, open(FILE_PATH, "rb"))}
    )
    response: dict = requests.post(
        url=detection_url, data=m, headers={"x-api-key": DETECTION_API_KEY}
    ).json()
    subject_response: dict = detection_service.detect(image_path=FILE_PATH)
    assert response == subject_response
