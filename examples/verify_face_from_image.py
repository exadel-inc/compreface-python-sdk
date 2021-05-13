# -*- coding: utf-8 -*-

from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.config.compreface_server_config import DOMAIN, PORT, RECOGNITION_API_KEY


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

face_collection: FaceCollection = recognition.get_face_collection()

face: dict = next(item for item in face_collection.list().get('faces') if item['subject'] ==
                  'Leonardo Wilhelm DiCaprio')

image_id = face.get('image_id')

print(face_collection.verify(image_path, image_id))
