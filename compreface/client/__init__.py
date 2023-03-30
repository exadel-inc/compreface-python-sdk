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

from .verification_face_from_image import VerificationFaceFromImageClient
from .add_example_of_subject import AddExampleOfSubjectClient
from .delete_example_by_id import DeleteExampleByIdClient
from .recognize_face_from_image import RecognizeFaceFromImageClient
from .detect_face_from_image import DetectFaceFromImageClient
from .verify_face_from_image import VerifyFaceFromImageClient
from .subject_client import SubjectClient
from .recognize_face_from_embeddings import RecognizeFaceFromEmbeddingClient
from .verification_face_from_embeddings import VerificationFaceFromEmbeddingClient
from .verify_face_from_embeddings import VerifyFaceFromEmbeddingClient
