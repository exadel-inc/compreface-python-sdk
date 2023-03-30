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

from compreface.common.typed_dict import (
    AllOptionsDict,
    ExpandedOptionsDict,
    DetProbOptionsDict,
    SavedObjectOptions,
    pass_dict,
)
from ..use_cases import (
    AddExampleOfSubject,
    AddSubject,
    DeleteAllExamplesOfSubjectByName,
    DeleteSubjectByName,
    DeleteAllSubjects,
    DeleteExampleById,
    DeleteExampleByIds,
    GetSubjects,
    UpdateSubject,
    VerificationFaceFromImage,
    VerificationFaceFromEmbedding,
    ListOfAllSavedSubjects,
)


class FaceCollection:
    def __init__(
        self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}
    ):
        """Init service with define API Key"""
        self.available_services = []
        self.api_key = api_key
        self.options = options
        self.add_example: AddExampleOfSubject = AddExampleOfSubject(
            domain=domain, port=port, api_key=api_key
        )
        self.list_of_all_saved_subjects: ListOfAllSavedSubjects = (
            ListOfAllSavedSubjects(domain=domain, port=port, api_key=api_key)
        )
        self.delete_all_examples_of_subject_by_name: DeleteAllExamplesOfSubjectByName = DeleteAllExamplesOfSubjectByName(
            domain=domain, port=port, api_key=api_key
        )
        self.delete_all_examples_by_id: DeleteExampleById = DeleteExampleById(
            domain=domain, port=port, api_key=api_key
        )
        self.delete_all_examples_by_ids: DeleteExampleByIds = DeleteExampleByIds(
            domain=domain, port=port, api_key=api_key
        )
        self.verify_face_from_image: VerificationFaceFromImage = (
            VerificationFaceFromImage(domain=domain, port=port, api_key=api_key)
        )
        self.verify_face_from_embeddings: VerificationFaceFromEmbedding = (
            VerificationFaceFromEmbedding(domain=domain, port=port, api_key=api_key)
        )

    def list(self, options: SavedObjectOptions = {}) -> dict:
        """
        Retrieve a list of subjects saved in a Face Collection

        :param options: Optional[dict]

        Options contains args:

        page int: page number of examples to return. Can be used for pagination. Default value is 0.
        size int: faces on page (page size). Can be used for pagination. Default value is 20.
        subject str: what subject examples endpoint should return. If empty, return examples for all subjects.

        :return:
        """
        return self.list_of_all_saved_subjects.execute(
            pass_dict(options, SavedObjectOptions) if options == {} else options
        )

    def add(
        self, image_path: str, subject: str, options: DetProbOptionsDict = {}
    ) -> dict:
        """
        This creates an example of the subject by saving images.
        You can add as many images as you want to train the system. Image should contain only one face.

        :param image_path: str, path to the image,
        allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb

        :param subject: str, it is the name you assign to the image you save
        :param options: dict[Optional]

        Options contains args:
        det_prob_threshold float: minimum required confidence that a recognized face is actually a face.
        Value is between 0.0 and 1.0.

        :return:
        """
        request = AddExampleOfSubject.Request(
            api_key=self.api_key, image_path=image_path, subject=subject
        )
        return self.add_example.execute(
            request,
            pass_dict(options, DetProbOptionsDict) if options == {} else options,
        )

    def delete(self, image_id: str) -> dict:
        """
        Delete an Example of the Subject by ID

        :param image_id: str or UUID of the removing face
        :return: dict
        """
        request = DeleteExampleById.Request(api_key=self.api_key, image_id=image_id)
        return self.delete_all_examples_by_id.execute(request)

    def delete_multiple(self, image_ids: list) -> dict:
        """
        Delete several subject examples.

        :param image_ids: list of str or UUID of the removing face.
        :return dict:
        """
        request = DeleteExampleByIds.Request(api_key=self.api_key, image_ids=image_ids)
        return self.delete_all_examples_by_ids.execute(request)

    def delete_all(self, subject: str) -> dict:
        """
        Delete All Examples of the Subject by Name

        :param subject: str, it is the name subject.
        If this parameter is absent, all faces in Face Collection will be removed.

        :return: dict
        """
        request = DeleteAllExamplesOfSubjectByName.Request(
            api_key=self.api_key, subject=subject
        )
        return self.delete_all_examples_of_subject_by_name.execute(request)

    def verify_image(
        self, image_path: str, image_id: str, options: ExpandedOptionsDict = {}
    ) -> dict:
        """
        Compare faces from the uploaded images with the face in saved image ID.

        :param image_path: str, path to the image,
        allowed image formats: jpeg, jpg, ico, png, bmp, gif, tif, tiff, webp. Max size is 5Mb

        :param image_id: str or UUID of the verifying face
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


        :return:  dict
        """
        request = VerificationFaceFromImage.Request(
            api_key=self.api_key, image_path=image_path, image_id=image_id
        )
        return self.verify_face_from_image.execute(
            request,
            pass_dict(options, ExpandedOptionsDict) if options == {} else options,
        )

    def verify_embeddings(self, embeddings: list, image_id: str) -> dict:
        """
        Compare input embeddings to the embedding stored in Face Collection.

        :param embeddings: list, an input embeddings. The length depends on the model (e.g. 512 or 128)
        :param image_id: str or UUID, an id of the source embedding within the Face Collection

        :return:  dict
        """
        request = VerificationFaceFromEmbedding.Request(
            api_key=self.api_key, embeddings=embeddings, image_id=image_id
        )

        return self.verify_face_from_embeddings.execute(request)


class Subjects:
    def __init__(
        self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}
    ):
        """Init service with define API Key"""
        self.available_services = []
        self.api_key = api_key
        self.options = options
        self.add_subject: AddSubject = AddSubject(
            domain=domain, port=port, api_key=api_key
        )
        self.update_subject: UpdateSubject = UpdateSubject(
            domain=domain, port=port, api_key=api_key
        )
        self.delete_subject: DeleteSubjectByName = DeleteSubjectByName(
            domain=domain, port=port, api_key=api_key
        )
        self.delete_all_subjects: DeleteAllSubjects = DeleteAllSubjects(
            domain=domain, port=port, api_key=api_key
        )
        self.list_of_all_saved_subjects: GetSubjects = GetSubjects(
            domain=domain, port=port, api_key=api_key
        )

    def list(self) -> dict:
        """
        This returns all subject related to Face Collection.

        :return:
        """
        return self.list_of_all_saved_subjects.execute()

    def add(self, subject: str) -> dict:
        """
        Create a new subject in Face Collection. Creating a subject is an optional step,
        you can upload an example without an existing subject, and a subject will be created automatically.

        :param subject: str, it is the name of the subject. It can be a person name, but it can be any string
        :return: dict
        """
        request = AddSubject.Request(subject=subject)
        return self.add_subject.execute(request)

    def update(self, subject: str, new_name: str) -> dict:
        """
        Rename existing subject. If a new subject name already exists,
        subjects are merged - all faces from the old subject name are reassigned to
        the subject with the new name, old subject removed.

        :param subject: str, existing subject
        :param new_name: str, it is the name of the subject. It can be a person name, but it can be any string
        :return: dict
        """
        request = UpdateSubject.Request(subject=new_name, api_endpoint=subject)
        return self.update_subject.execute(request)

    def delete(self, subject: str) -> dict:
        """
        Delete existing subject and all saved faces.

        :param subject: str,it is the name of the subject. It can be a person name, but it can be any string
        :return: dict
        """
        request = DeleteSubjectByName.Request(subject=subject)
        return self.delete_subject.execute(request)

    def delete_all(self) -> dict:
        """
        Delete all existing subjects and all saved faces.

        :return: dict
        """
        return self.delete_all_subjects.execute()
