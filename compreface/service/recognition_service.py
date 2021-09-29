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

from compreface.common.typed_dict import AllOptionsDict
from typing import List

from ..common import Service
from ..collections import FaceCollection, Subjects
from ..use_cases import RecognizeFaceFromImage


class RecognitionService(Service):
    """Recognition service"""

    def __init__(self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}):
        """Init service with define API Key"""
        super().__init__(api_key, options)
        self.available_services = []
        self.recognize_face_from_images: RecognizeFaceFromImage = RecognizeFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.face_collection: FaceCollection = FaceCollection(
            domain=domain,
            port=port,
            api_key=api_key,
            options=options
        )
        self.subjects: Subjects = Subjects(
            domain=domain,
            port=port,
            api_key=api_key,
            options=options
        )

    def get_available_functions(self) -> List[str]:
        """
        Get List of available functions in service
        :return:
        """
        return self.available_services

    def recognize(self, image_path: str, options: AllOptionsDict = {}) -> dict:
        """
        Recognize image
        :param image_path:
        :param options:
        :return:
        """
        request = RecognizeFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path
        )
        return self.recognize_face_from_images.execute(request, self.options if options == {} else options)

    def get_face_collection(self) -> FaceCollection:
        """
        Get face collection
        :return:
        """
        return self.face_collection

    def get_subjects(self) -> Subjects:
        """
        Get subjects
        :return:
        """
        return self.subjects
