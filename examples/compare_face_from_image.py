# -*- coding: utf-8 -*-

from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import RecognitionService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
RECOGNITION_API_KEY: str = '9916f5d1-216f-4049-9e06-51c140bfa898'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

face_collection: FaceCollection = recognition.get_face_collection()

face: dict = next(item for item in face_collection.list().get('faces') if item['subject'] ==
                  'Leonardo Wilhelm DiCaprio')

image_id = face.get('image_id')

print(face_collection.compare(image_path, image_id, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "status": "true"
}))
