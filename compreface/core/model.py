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

from typing import Optional
from ..service import (
    RecognitionService,
    VerificationService,
    DetectionService
)


class CompreFace(object):
    """
    Main class
    """

    def __init__(self, domain: str, port: str):
        self._domain: str = domain
        self._port: str = port
        self.recognition: Optional[RecognitionService] = None
        self.verification: Optional[VerificationService] = None
        self.detection: Optional[DetectionService] = None

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        self._domain = domain

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port: str):
        self._port = port

    def init_face_recognition(self, api_key: str) -> RecognitionService:
        """
        Init Face Recognition Service
        :param api_key:
        :return:
        """
        self.recognition = RecognitionService(api_key=api_key,
                                              domain=self.domain,
                                              port=self.port)
        return self.recognition

    def init_face_verification(self, api_key: str) -> VerificationService:
        """
        Init Face Verification Service
        :param api_key:
        :return:
        """
        self.verification = VerificationService(api_key=api_key,
                                                domain=self.domain,
                                                port=self.port)
        return self.verification

    def init_face_detection(self, api_key: str) -> DetectionService:
        """
        Init Face Detection Service
        :param api_key:
        :return:
        """
        self.detection = DetectionService(api_key=api_key, domain=self.domain,
                                          port=self.port)
        return self.detection
