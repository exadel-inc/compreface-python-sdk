from compreface.collections.face_collections import FaceCollection
from compreface import CompreFace
from compreface.service import DetectionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'a482a613-3118-4554-a295-153bd6e8ac65'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_recognition(
    DETECTION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

face_collection: FaceCollection = detection.get_face_collection()

print(face_collection.detect(image_path))
