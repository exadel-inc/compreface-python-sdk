# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import AddExampleOfSubjectClient


class DeleteAllExamplesOfSubjectByName:

    @dataclass
    class Request:
        api_key: str
        subject: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.add_example_of_subject = AddExampleOfSubjectClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request) -> dict:
        result: dict = self.add_example_of_subject.delete(request.subject)
        return result
