# -*- coding: utf-8 -*-

from typing import List

from ..common import Service
from ..collections import FaceCollection
from ..use_cases import (
    RecognizeFaceFromImage,
    VerifyFaceFromImage
)


class RecognitionService(Service):
    """Recognition service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = []
        self.verify_face_from_image: VerifyFaceFromImage = VerifyFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )
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

    def verify(self, image_path: str, image_id: str, limit: int = 0, det_prob_threshold: float = 0.8) -> dict:
        """
        Verify image
        :param image_path:
        :param image_id:
        :param limit:
        :param det_prob_threshold:
        :return:
        """
        request = VerifyFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path,
            image_id=image_id,
            limit=limit,
            det_prob_threshold=det_prob_threshold
        )
        return self.verify_face_from_image.execute(request)

    def recognize(self, image_path: str, limit: float = 0, det_prob_threshold: float = 0.8,
                  prediction_count: int = 1) -> dict:
        """
        Recognize image
        :param image_path:
        :param limit:
        :param det_prob_threshold:
        :param prediction_count:
        :return:
        """
        request = RecognizeFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path,
            limit=limit,
            det_prob_threshold=det_prob_threshold,
            prediction_count=prediction_count
        )
        return self.recognize_face_from_images.execute(request)

    def get_face_collection(self) -> FaceCollection:
        """
        Get face collection
        :return:
        """
        return self.face_collection
