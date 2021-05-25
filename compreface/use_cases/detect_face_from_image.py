from compreface.common.typed_dict import AllOptionsDict
from dataclasses import dataclass
from ..client import DetectFaceFromImageClient


class DetectFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        image_path: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.detect_face_from_image = DetectFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request, options: AllOptionsDict = {}) -> dict:
        result: dict = self.detect_face_from_image.post(
            request.image_path, options)
        return result
