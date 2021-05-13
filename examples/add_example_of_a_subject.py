# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.config.compreface_server_config import DOMAIN, PORT, RECOGNITION_API_KEY


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

image_path: str = 'examples/common/di_kaprio.jpg'
subject: str = 'Leonardo Wilhelm DiCaprio'

print(face_collection.add(image_path, subject))
