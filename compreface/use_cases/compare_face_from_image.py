# -*- coding: utf-8 -*-

from compreface.common.typed_dict import ExpandedOptionsDict
from dataclasses import dataclass
from ..client import CompareFaceFromImageClient


class CompareFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        image_path: str
        image_id: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.verify_face_from_image = CompareFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request, options: ExpandedOptionsDict = {}):
        result: dict = self.verify_face_from_image.post(request.image_path,
                                                        request.image_id, options)
        return result
