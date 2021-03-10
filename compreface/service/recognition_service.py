# -*- coding: utf-8 -*-

from typing import List

from ..common import Service
from ..use_cases import (
    AddExampleOfSubject,
    RecognizeFaceFromImage,
    ListOfAllSavedSubjects,
    DeleteAllExamplesOfSubjectByName,
    DeleteExampleById
)


class RecognitionService(Service):
    """Recognition service"""

    def __init__(self, api_key: str, domain: str, port: str):
        """Init service with define API Key"""
        super().__init__(api_key)
        self.available_services = ['']
        self.add_example: AddExampleOfSubject = AddExampleOfSubject(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.recognize_face_from_images: RecognizeFaceFromImage = RecognizeFaceFromImage(
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

    def get_available_functions(self) -> List[str]:
        """
        Get List of available functions in service
        :return:
        """
        return self.available_services

    def add_example_of_subject(self, image_path: str, subject: str) -> dict:
        """

        :param image_path:
        :param subject:
        :return:
        """
        request = AddExampleOfSubject.Request(
            api_key=self.api_key,
            image_path=image_path,
            subject=subject
        )
        return self.add_example.execute(request)

    def recognize_face(self, image_path: str, limit: float = 0, det_prob_threshold: float = 0.8,
                       prediction_count: int = 1) -> dict:
        """

        :param image_path:
        :param limit:
        :param det_prob_threshold:
        :param prediction_count:
        :return:
        """
        request = RecognizeFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path,
            limit=limit,
            det_prob_threshold=det_prob_threshold,
            prediction_count=prediction_count
        )
        return self.recognize_face_from_images.execute(request)

    def get_list_of_subjects(self) -> dict:
        """

        :return:
        """
        return self.list_of_all_saved_subjects.execute()

    def delete_all_examples_of_subject(self, subject: str) -> dict:
        """

        :param subject:
        :return:
        """
        request = DeleteAllExamplesOfSubjectByName.Request(
            api_key=self.api_key,
            subject=subject
        )
        return self.delete_all_examples_of_subject_by_name.execute(request)

    def delete_example(self, image_id: str) -> dict:
        """

        :param image_id:
        :return:
        """
        request = DeleteExampleById.Request(
            api_key=self.api_key,
            image_id=image_id
        )
        return self.delete_all_examples_by_id.execute(request)
