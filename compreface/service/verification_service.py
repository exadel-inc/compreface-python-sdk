# -*- coding: utf-8 -*-

from typing import List

from ..common import Service
from ..use_cases import VerifyFaceFromImage


class VerificationService(Service):
    """Verification service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = []
        self.verify_face_from_image: VerifyFaceFromImage = VerifyFaceFromImage(
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

    def verify_face(self, image_path: str, image_id: str, limit: int = 0, det_prob_threshold: float = 0.8) -> dict:
        """

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
