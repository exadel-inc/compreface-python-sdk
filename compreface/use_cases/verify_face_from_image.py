# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import VerifyFaceFromImageClient


class VerifyFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        image_path: str
        image_id: str
        limit: float = 0
        det_prob_threshold: float = 0.8

    def __init__(self, domain: str, port: str, api_key: str):
        self.verify_face_from_image = VerifyFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request):
        result: dict = self.verify_face_from_image.post(request.image_path,
                                                        request.image_id,
                                                        request.limit,
                                                        request.det_prob_threshold)
        return result
