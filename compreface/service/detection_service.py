# -*- coding: utf-8 -*-

from compreface.common.typed_dict import AllOptionsDict
from compreface.use_cases.detect_face_from_image import DetectFaceFromImage
from typing import List

from ..common import Service


class DetectionService(Service):
    """Detection service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
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

    def detect(self, image_path: str, options: AllOptionsDict = {}) -> dict:
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
        return self.detect_face_from_image.execute(request, options)
