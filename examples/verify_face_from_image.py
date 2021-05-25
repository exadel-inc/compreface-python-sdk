from compreface import CompreFace
from compreface.service import VerificationService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
VERIFICATION_API_KEY: str = '3c6171a4-e115-41f0-afda-4032bda4bfe9'


compre_face: CompreFace = CompreFace(DOMAIN, PORT)

verify: VerificationService = compre_face.init_face_verification(
    VERIFICATION_API_KEY)

image_path: str = 'examples/common/di_kaprio.jpg'


print(verify.verify(image_path, image_path, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "prediction_count": 1,
    "face_plugins": "age,gender",
    "status": "true"
}))
