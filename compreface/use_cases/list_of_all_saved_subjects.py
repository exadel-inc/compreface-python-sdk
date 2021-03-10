# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import AddExampleOfSubjectClient


class ListOfAllSavedSubjects:

    @dataclass
    class Request:
        pass

    def __init__(self, domain: str, port: str, api_key: str):
        self.add_example_of_subject = AddExampleOfSubjectClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self) -> dict:
        result: dict = self.add_example_of_subject.get()
        return result
