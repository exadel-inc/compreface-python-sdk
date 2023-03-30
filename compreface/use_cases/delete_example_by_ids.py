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

from dataclasses import dataclass
from ..client import DeleteExampleByIdClient


class DeleteExampleByIds:
    @dataclass
    class Request:
        api_key: str
        image_ids: list

    def __init__(self, domain: str, port: str, api_key: str):
        self.delete_example_by_id = DeleteExampleByIdClient(
            api_key=api_key, domain=domain, port=port
        )

    def execute(self, request: Request):
        result: dict = self.delete_example_by_id.post(request.image_ids)
        return result
