# -*- coding: utf-8 -*-

from compreface.use_cases.verifiy_face_from_images import VerifyFaceFromImage
from requests.api import request
from compreface.common.typed_dict import AllOptionsDict
from compreface.client.verify_face_from_image import VerifyFaceFromImageClient
from compreface.collections.face_collections import FaceCollection
from typing import List

from ..common import Service


class VerificationService(Service):
    """Verification service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = []
        self.verify_face_from_image: VerifyFaceFromImageClient = VerifyFaceFromImageClient(
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

    def verify(self, source_image_path: str, target_image_path: str, options: AllOptionsDict) -> dict:
        """
        Verify face in images
        :param source_image_path:
        :param target_image_path:
        :param options:
        :return:
        """
        request = VerifyFaceFromImage.Request(api_key=self.api_key,
                                              source_image_path=source_image_path,
                                              target_image_path=target_image_path)
        return self.verify_face_from_image.post(
            source_image_path=request.source_image_path,
            target_image_path=request.target_image_path,
            options=options
        )
