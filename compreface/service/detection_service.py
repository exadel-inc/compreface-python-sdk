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

from compreface.common.typed_dict import AllOptionsDict, ExpandedOptionsDict, pass_dict
from compreface.use_cases.detect_face_from_image import DetectFaceFromImage
from typing import List

from ..common import Service


class DetectionService(Service):
    """Detection service"""

    def __init__(self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}):
        """Init service with define API Key"""
        super().__init__(api_key, options)
        self.available_services = []
        self.detect_face_from_image: DetectFaceFromImage = DetectFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )

    def get_available_functions(self) -> List[str]:
        """
        Get List of available functions in service
        :return:
        """
        return self.available_services

    def detect(self, image_path: str, options: ExpandedOptionsDict = {}) -> dict:
        """
        Detect face in image
        :param image_path:
        :param options:
        :return:
        """
        request = DetectFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path
        )
        return self.detect_face_from_image.execute(request, pass_dict(
            self.options, ExpandedOptionsDict) if options == {} else options)
