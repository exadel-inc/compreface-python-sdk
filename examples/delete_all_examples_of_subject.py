# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.config.compreface_server_config import DOMAIN, PORT, RECOGNITION_API_KEY


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)
subject: str = 'Leonardo Wilhelm DiCaprio'

face_collection: FaceCollection = recognition.get_face_collection()

print(face_collection.delete_all(subject))
