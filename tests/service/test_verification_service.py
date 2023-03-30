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

from compreface.config.api_list import VERIFICATION_API, VERIFICATION_EMBEDDINGS_API
from tests.client.const_config import DOMAIN, PORT, VERIFICATION_API_KEY, FILE_PATH
from compreface.service.verification_service import VerificationService

url: str = DOMAIN + ":" + PORT + VERIFICATION_API

verification_service = VerificationService(
    api_key=VERIFICATION_API_KEY, domain=DOMAIN, port=PORT
)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize_image_recognition_servce():
    httpretty.register_uri(
        httpretty.POST,
        url + "/verify",
        headers={
            "x-api-key": VERIFICATION_API_KEY,
            "Content-Type": "multipart/form-data",
        },
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={
            "source_image": (name_img, open(FILE_PATH, "rb")),
            "target_image": (name_img, open(FILE_PATH, "rb")),
        }
    )
    response: dict = requests.post(
        url=url + "/verify",
        data=m,
        headers={"x-api-key": VERIFICATION_API_KEY, "Content-Type": m.content_type},
    ).json()
    subject_response: dict = verification_service.verify_image(FILE_PATH, FILE_PATH)
    assert response == subject_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_verify_embedding_recognition_service():
    embeddings_url: str = DOMAIN + ":" + PORT + VERIFICATION_EMBEDDINGS_API + "/verify"
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


def test_get_available_functions_recognition_service():
    assert verification_service.get_available_functions() == []
