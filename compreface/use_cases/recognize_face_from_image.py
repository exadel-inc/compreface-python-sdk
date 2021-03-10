# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import RecognizeFaceFromImageClient


class RecognizeFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        image_path: str
        limit: float = 0
        det_prob_threshold: float = 0.8
        prediction_count: int = 1

    def __init__(self, domain: str, port: str, api_key: str):
        self.recognize_face_from_image = RecognizeFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request) -> dict:
        result: dict = self.recognize_face_from_image.post(request.image_path,
                                                           request.limit,
                                                           request.det_prob_threshold,
                                                           request.prediction_count)
        return result
