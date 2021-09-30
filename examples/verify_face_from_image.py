"""
    Copyright(c) 2021 the original author or authors

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        https: // www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
    or implied. See the License for the specific language governing
    permissions and limitations under the License.
 """

from compreface import CompreFace
from compreface.service import VerificationService

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
VERIFICATION_API_KEY: str = '5c765423-4192-4fe8-9c60-092f495a332a'


compre_face: CompreFace = CompreFace(DOMAIN, PORT, {
    "limit": 0,
    "det_prob_threshold": 0.8,
    "face_plugins": "age,gender",
    "status": "true"
})

verify: VerificationService = compre_face.init_face_verification(
    VERIFICATION_API_KEY)

image_path: str = 'common/jonathan-petit-unsplash.jpg'

print(verify.verify(image_path, image_path))
