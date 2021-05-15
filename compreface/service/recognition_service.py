# -*- coding: utf-8 -*-

from typing import List

from ..common import Service
from ..collections import FaceCollection
from ..use_cases import (
    RecognizeFaceFromImage
)


class RecognitionService(Service):
    """Recognition service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = []
        self.recognize_face_from_images: RecognizeFaceFromImage = RecognizeFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.face_collection: FaceCollection = FaceCollection(
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

    def recognize(self, image_path: str, options: dict = {}) -> dict:
        """
        Recognize image
        :param image_path:
        :return:
        """
        request = RecognizeFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path
        )
        return self.recognize_face_from_images.execute(request, options)

    def get_face_collection(self) -> FaceCollection:
        """
        Get face collection
        :return:
        """
        return self.face_collection
