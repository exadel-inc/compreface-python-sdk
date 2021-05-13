# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

print(face_collection.list())
