from compreface import CompreFace
from compreface.service import DetectionService


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
DETECTION_API_KEY: str = 'a482a613-3118-4554-a295-153bd6e8ac65'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

detection: DetectionService = compre_face.init_face_detection(
    DETECTION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'

print(detection.detect(image_path, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "age,gender",
    "status": "true"
}))
