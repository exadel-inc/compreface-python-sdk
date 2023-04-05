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
from requests_toolbelt.multipart.encoder import MultipartEncoder

from compreface.collections.face_collections import FaceCollection
from compreface.config.api_list import RECOGNIZE_CRUD_API, RECOGNIZE_EMBEDDINGS_API
from tests.client.const_config import (
    DOMAIN,
    FILE_PATH,
    IMAGE_ID,
    PORT,
    RECOGNIZE_API_KEY,
)

url: str = DOMAIN + ":" + PORT + RECOGNIZE_CRUD_API

face_collection: FaceCollection = FaceCollection(
    api_key=RECOGNIZE_API_KEY, domain=DOMAIN, port=PORT
)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_list_face_collection():
    httpretty.register_uri(
        httpretty.GET,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='["Subject1", "Subject2"]',
    )
    response: dict = requests.get(
        url=url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()
    subject_response: dict = face_collection.list()
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_add_face_collection():
    httpretty.register_uri(
        httpretty.POST,
        url,
        headers={"x-api-key": RECOGNIZE_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"image_id": "image_id_subject", "subject": "Subject"}',
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
    subject_response: dict = face_collection.add(FILE_PATH, "Subject")
    assert subject_response == response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_face_collection():
    delete_url: str = url + "/" + IMAGE_ID
    httpretty.register_uri(
        httpretty.DELETE,
        delete_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.delete(
        url=delete_url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_response: dict = face_collection.delete(IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_all_face_collection():
    delete_url: str = url + "?subject=Subject1"
    httpretty.register_uri(
        httpretty.DELETE,
        delete_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.delete(
        url=delete_url, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_response: dict = face_collection.delete_all("Subject1")
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_delete_multiple_face_collection():
    delete_url: str = url + "/delete"
    image_ids: list = ["1", "2", "3"]
    httpretty.register_uri(
        httpretty.POST,
        delete_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"image_id": "image_id", "subject": "Donatello"}',
    )
    response: dict = requests.post(
        url=delete_url, json=image_ids, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()

    test_response: dict = face_collection.delete_multiple(image_ids)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_verify_image_face_collection():
    verify_url: str = url + "/" + IMAGE_ID + "/verify"
    httpretty.register_uri(
        httpretty.POST,
        verify_url,
        headers={"x-api-key": RECOGNIZE_API_KEY, "Content-Type": "multipart/form-data"},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    name_img: str = os.path.basename(FILE_PATH)
    m: MultipartEncoder = MultipartEncoder(
        fields={"file": (name_img, open(FILE_PATH, "rb"))}
    )
    response: dict = requests.post(
        url=verify_url, data=m, headers={"x-api-key": RECOGNIZE_API_KEY}
    ).json()
    test_response: dict = face_collection.verify_image(FILE_PATH, IMAGE_ID)
    assert response == test_response


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_verify_embeddings_face_collection():
    embedding: list = [1, 6, 7, 2]
    verify_url: str = (
        DOMAIN
        + ":"
        + PORT
        + RECOGNIZE_EMBEDDINGS_API
        + "/faces/"
        + IMAGE_ID
        + "/verify"
    )
    httpretty.register_uri(
        httpretty.POST,
        verify_url,
        headers={"x-api-key": RECOGNIZE_API_KEY},
        body='{"result" : [{"age" : [ 25, 32 ], "gender" : "male"}]}',
    )

    response: dict = requests.post(
        url=verify_url,
        json={"embeddings": embedding},
        headers={"x-api-key": RECOGNIZE_API_KEY},
    ).json()
    test_response: dict = face_collection.verify_embeddings(embedding, IMAGE_ID)
    assert response == test_response
