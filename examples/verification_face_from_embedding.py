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

from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = "http://localhost"
PORT: str = "8000"
RECOGNITION_API_KEY: str = "00000000-0000-0000-0000-000000000002"

compre_face: CompreFace = CompreFace(
    DOMAIN, PORT, {"limit": 0, "det_prob_threshold": 0.8, "status": "true"}
)

recognition: RecognitionService = compre_face.init_face_recognition(RECOGNITION_API_KEY)

image_path: str = "examples/common/jonathan-petit-unsplash.jpg"

face_collection: FaceCollection = recognition.get_face_collection()

print(face_collection.list())

result = recognition.recognize_image(
    image_path,
    options={
        "limit": 0,
        "det_prob_threshold": 0.8,
        "face_plugins": "calculator",
        "status": "true",
    },
).get("result")

face: dict = next(
    item
    for item in face_collection.list().get("faces")
    if item["subject"] == "Jonathan Petit"
)

image_id = face.get("image_id")

if len(result) != 0:
    last_result: dict = result[len(result) - 1]
    embeddings: list = last_result.get("embedding", [])
    print(face_collection.verify_embeddings([embeddings], image_id))
else:
    print("No embedding found")
