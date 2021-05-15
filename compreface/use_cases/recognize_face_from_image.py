# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import RecognizeFaceFromImageClient


class RecognizeFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        image_path: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.recognize_face_from_image = RecognizeFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request, options: dict = {}) -> dict:
        result: dict = self.recognize_face_from_image.post(
            request.image_path, options)
        return result
