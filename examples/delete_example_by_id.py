# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.config.compreface_server_config import DOMAIN, PORT, RECOGNITION_API_KEY


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
