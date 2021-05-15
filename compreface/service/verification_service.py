# -*- coding: utf-8 -*-

from compreface.collections.face_collections import FaceCollection
from typing import List

from ..common import Service


class VerificationService(Service):
    """Verification service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = []
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
