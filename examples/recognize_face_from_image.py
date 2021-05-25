# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

print(recognition.recognize(image_path, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
}))
