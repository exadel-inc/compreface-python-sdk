# -*- coding: utf-8 -*-

from compreface.common.typed_dict import DetProbOptionsDict
from dataclasses import dataclass
from ..client import AddExampleOfSubjectClient


class AddExampleOfSubject:

    @dataclass
    class Request:
        api_key: str
        image_path: str
        subject: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.add_example_of_subject = AddExampleOfSubjectClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request, options: DetProbOptionsDict = {}) -> dict:
        result: dict = self.add_example_of_subject.post(
            request.image_path, request.subject, options)
        return result
