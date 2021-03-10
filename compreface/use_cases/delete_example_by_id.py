# -*- coding: utf-8 -*-

from dataclasses import dataclass
from ..client import DeleteExampleByIdClient


class DeleteExampleById:

    @dataclass
    class Request:
        api_key: str
        image_id: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.delete_example_by_id = DeleteExampleByIdClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request):
        result: dict = self.delete_example_by_id.delete(request.image_id)
        return result
