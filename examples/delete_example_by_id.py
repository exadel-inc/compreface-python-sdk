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

faces: list = face_collection.list().get('faces')

if(len(faces) != 0):
    last_face: dict = faces[len(faces) - 1]
    print(face_collection.delete(last_face.get('image_id')))
else:
    print('No subject found')
