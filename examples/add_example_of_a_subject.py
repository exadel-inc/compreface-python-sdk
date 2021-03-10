# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '7dacfc8e-1bb1-4fcf-a9b1-76e4d9d89855'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

image_path: str = '/home/aliubymov/A-OZSXlgs3c.jpg'
subject: str = 'test'
print(recognition.add_example_of_subject(image_path, subject))
