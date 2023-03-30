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

from compreface.use_cases.verify_face_from_images import VerifyFaceFromImage
from compreface.use_cases.verify_face_from_embedding import VerifyFaceFromEmbedding
from compreface.common.typed_dict import AllOptionsDict, ExpandedOptionsDict, pass_dict
from typing import List

from ..common import Service


class VerificationService(Service):
    """Verification service"""

    def __init__(
        self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}
    ):
        """Init service with define API Key"""
        super().__init__(api_key, options)
        self.available_services = []
        self.verify_face_from_image: VerifyFaceFromImage = VerifyFaceFromImage(
            domain=domain, port=port, api_key=api_key
        )
        self.verify_face_from_embedding: VerifyFaceFromEmbedding = (
            VerifyFaceFromEmbedding(domain=domain, api_key=api_key, port=port)
        )

    def get_available_functions(self) -> List[str]:
        """
        Get List of available functions in service
        :return:
        """
        return self.available_services

    def verify_image(
        self,
        source_image_path: str,
        target_image_path: str,
        options: ExpandedOptionsDict = {},
    ) -> dict:
        """
        Verify face to compare faces from given two images

        :param source_image_path: file to be verified.
        Allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb

        :param target_image_path: reference file to check the source file.
        Allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb

        :param options: dict, Optional.

        Options contains args:
        limit int: maximum number of faces on the target image to be recognized.
        It recognizes the biggest faces first. Value of 0 represents no limit.
        Default value: 0

        det_prob_threshold float: minimum required confidence that a recognized face is actually a face.
        Value is between 0.0 and 1.0.

        face_plugins str: comma-separated slugs of face plugins.
        If empty, no additional information is returned.

        status bool: if true includes system information like execution_time and plugin_version fields.
        Default value is false

        :return: dict
        """
        request = VerifyFaceFromImage.Request(
            api_key=self.api_key,
            source_image_path=source_image_path,
            target_image_path=target_image_path,
        )
        return self.verify_face_from_image.execute(
            request=request,
            options=pass_dict(self.options, ExpandedOptionsDict)
            if options == {}
            else options,
        )

    def verify_embedding(
        self, source_embeddings: list, targets_embeddings: list
    ) -> dict:
        """
        Verify face from given embeddings

        :param source_embeddings: An input embeddings. The length depends on the model.
        :param targets_embeddings: An array of the target embeddings. The length depends on the model.

        :return: dict
        """
        request = VerifyFaceFromEmbedding.Request(
            api_key=self.api_key,
            source_embeddings=source_embeddings,
            targets_embeddings=targets_embeddings,
        )

        return self.verify_face_from_embedding.execute(request=request)
