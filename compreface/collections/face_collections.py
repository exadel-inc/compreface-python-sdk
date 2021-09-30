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

from compreface.common.typed_dict import AllOptionsDict, ExpandedOptionsDict, DetProbOptionsDict, pass_dict
from ..use_cases import (
    AddExampleOfSubject,
    AddSubject,
    DeleteAllExamplesOfSubjectByName,
    DeleteSubjectByName,
    DeleteAllSubjects,
    DeleteExampleById,
    GetSubjects,
    UpdateSubject,
    VerificationFaceFromImage,
    ListOfAllSavedSubjects
)


class FaceCollection:
    def __init__(self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}):
        """Init service with define API Key"""
        self.available_services = []
        self.api_key = api_key
        self.options = options
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
        self.verify_face_from_image: VerificationFaceFromImage = VerificationFaceFromImage(
            domain=domain,
            port=port,
            api_key=api_key
        )

    def list(self) -> dict:
        """
        Get list of collections
        :return:
        """
        return self.list_of_all_saved_subjects.execute()

    def add(self, image_path: str, subject: str, options: DetProbOptionsDict = {}) -> dict:
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
        return self.add_example.execute(request, pass_dict(options, DetProbOptionsDict) if options == {} else options)

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

    def verify(self, image_path: str, image_id: str, options: ExpandedOptionsDict = {}) -> dict:
        """
        Compare image
        :param image_path:
        :param image_id:
        :return:
        """
        request = VerificationFaceFromImage.Request(
            api_key=self.api_key,
            image_path=image_path,
            image_id=image_id
        )
        return self.verify_face_from_image.execute(request, pass_dict(options, ExpandedOptionsDict) if options == {} else options)


class Subjects:
    def __init__(self, api_key: str, domain: str, port: str, options: AllOptionsDict = {}):
        """Init service with define API Key"""
        self.available_services = []
        self.api_key = api_key
        self.options = options
        self.add_subject: AddSubject = AddSubject(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.update_subject: UpdateSubject = UpdateSubject(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.delete_subject: DeleteSubjectByName = DeleteSubjectByName(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.delete_all_subjects: DeleteAllSubjects = DeleteAllSubjects(
            domain=domain,
            port=port,
            api_key=api_key
        )
        self.list_of_all_saved_subjects: GetSubjects = GetSubjects(
            domain=domain,
            port=port,
            api_key=api_key
        )

    def list(self) -> dict:
        """
        Get list of subjects
        :return:
        """
        return self.list_of_all_saved_subjects.execute()

    def add(self, subject: str) -> dict:
        """
        Add subject
        :param subject:
        :return:
        """
        request = AddSubject.Request(
            subject=subject
        )
        return self.add_subject.execute(request)

    def update(self, subject: str, new_name: str) -> dict:
        """
        Update subject by name
        :param subject:
        :param new_name:
        :return:
        """
        request = UpdateSubject.Request(
            subject=new_name,
            api_endpoint=subject
        )
        return self.update_subject.execute(request)

    def delete(self, subject: str) -> dict:
        """
        Delete subject by name
        :param subject:
        :return:
        """
        request = DeleteSubjectByName.Request(
            subject=subject
        )
        return self.delete_subject.execute(request)

    def delete_all(self) -> dict:
        """
        Delete all subjects
        :return:
        """
        return self.delete_all_subjects.execute()
