
from requests.api import request
from compreface.use_cases.verify_face_from_image import VerifyFaceFromImage
from ..use_cases import (
    AddExampleOfSubject,
    ListOfAllSavedSubjects,
    DeleteAllExamplesOfSubjectByName,
    DeleteExampleById,
    DetectFaceFromImage
)


class FaceCollection:
    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        self.available_services = []
        self.api_key = api_key
        self.add_example: AddExampleOfSubject = AddExampleOfSubject(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.list_of_all_saved_subjects: ListOfAllSavedSubjects = ListOfAllSavedSubjects(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.delete_all_examples_of_subject_by_name: DeleteAllExamplesOfSubjectByName = DeleteAllExamplesOfSubjectByName(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.delete_all_examples_by_id: DeleteExampleById = DeleteExampleById(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.verify_face_from_image: VerifyFaceFromImage = VerifyFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.detect_face_from_image: DetectFaceFromImage = DetectFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )

    def add(self, image_path: str, subject: str, options: dict = {}) -> dict:
        """
        Add example to collection
        :param image_path:
        :param subject:
        :return:
        """
        request = AddExampleOfSubject.Request(
            api_key=self.api_key,
            image_path=image_path,
            subject=subject
        )
        return self.add_example.execute(request, options)

    def list(self) -> dict:
        """
        Get list of collections
        :return:
        """
        return self.list_of_all_saved_subjects.execute()

    def delete_all(self, subject: str) -> dict:
        """
        Delete all examples of subject
        :param subject:
        :return:
        """
        request = DeleteAllExamplesOfSubjectByName.Request(
            api_key=self.api_key,
            subject=subject
        )
        return self.delete_all_examples_of_subject_by_name.execute(request)

    def delete(self, image_id: str) -> dict:
        """
        Delete example by Id
        :param image_id:
        :return:
        """
        request = DeleteExampleById.Request(
            api_key=self.api_key,
            image_id=image_id
        )
        return self.delete_all_examples_by_id.execute(request)

    def verify(self, image_path: str, image_id: str, options: dict = {}) -> dict:
        """
        Verify image
        :param image_path:
        :param image_id:
        :return:
        """
        request = VerifyFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path,
            image_id=image_id
        )
        return self.verify_face_from_image.execute(request, options)

    def detect(self, image_path: str, options: dict = {}) -> dict:
        """
        Detect face in image
        :param image_path:
        :return:
        """
        request = DetectFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path
        )
        return self.detect_face_from_image.execute(request, options)
