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
from compreface.collections.face_collections import FaceCollection, Subjects

from compreface.config.api_list import (
    RECOGNIZE_API,
    RECOGNIZE_EMBEDDINGS_API,
    RECOGNIZE_CRUD_API,
    SUBJECTS_CRUD_API,
)
from tests.client.const_config import DOMAIN, PORT, RECOGNIZE_API_KEY, FILE_PATH
from compreface.service.recognition_service import RecognitionService

url: str = DOMAIN + ":" + PORT + RECOGNIZE_API

recognition_service = RecognitionService(
    api_key=RECOGNIZE_API_KEY, domain=DOMAIN, port=PORT
)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_face_collection_recognition_service():
    face_collection_url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API
    httpretty.register_uri(
        httpretty.GET,
        face_collection_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1", "Subject2"]',
    )
    face_collection_expected = FaceCollection(
        api_key=RECOGNIZE_API_KEY, domain=DOMAIN, port=PORT
    )
    face_collection_actual = recognition_service.get_face_collection()

    subject_response: dict = face_collection_expected.list()
    response: dict = face_collection_actual.list()

    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_subjects_recognition_service():
    httpretty.register_uri(
        httpretty.GET,
        DOMAIN + ":" + PORT + SUBJECTS_CRUD_API,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1", "Subject2"]',
    )
    subject = Subjects(api_key=RECOGNIZE_API_KEY, domain=DOMAIN, port=PORT)
    subject_expected = recognition_service.get_subjects()

    response: dict = subject.list()
    subject_response: dict = subject_expected.list()

    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize_image_recognition_servce():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )
    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={"file": (name_img, open(FILE_PATH, "rb"))}
    )
    response: dict = requests.post(
        url=url,
        data=m,
        headers={"x-api-key": RECOGNIZE_API_KEY, "Content-Type": "multipart/form-data"},
    ).json()
    subject_response: dict = recognition_service.recognize_image(FILE_PATH)
    assert response == subject_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_recognize_embeddings_recognition_service():
    embeddings: list = [2, 5, 6]
    embeddings_url: str = DOMAIN + ":" + PORT + RECOGNIZE_EMBEDDINGS_API + "/recognize"
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
    subject_response: dict = recognition_service.recognize_embedding(embeddings)
    assert response == subject_response


def test_get_available_functions_recognition_service():
    assert recognition_service.get_available_functions() == []
