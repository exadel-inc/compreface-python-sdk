# -*- coding: utf-8 -*-

from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.config.compreface_server_config import DOMAIN, PORT, RECOGNITION_API_KEY


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(
    RECOGNITION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

print(recognition.recognize(image_path))
