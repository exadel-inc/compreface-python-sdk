# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceColliction


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)
subject: str = 'test'

face_collection: FaceColliction = recognition.get_face_collection()

print(recognition.delete_all(subject))
