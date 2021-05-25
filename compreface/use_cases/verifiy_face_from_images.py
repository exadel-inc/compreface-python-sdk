from compreface.client.verify_face_from_image import VerifyFaceFromImageClient
from compreface.common.typed_dict import AllOptionsDict
from dataclasses import dataclass


class VerifyFaceFromImage:

    @dataclass
    class Request:
        api_key: str
        source_image_path: str
        target_image_path: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.verify_face_from_image = VerifyFaceFromImageClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request, options: AllOptionsDict = {}):
        result: dict = self.verify_face_from_image.post(request.source_image_path,
                                                        request.target_image_path,
                                                        options)
        return result
