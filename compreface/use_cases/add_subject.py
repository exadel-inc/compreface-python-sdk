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

from dataclasses import dataclass, asdict

from compreface.client.subject_client import SubjectClient


class AddSubject:

    @dataclass
    class Request:
        subject: str

    def __init__(self, domain: str, port: str, api_key: str):
        self.subject_client = SubjectClient(
            api_key=api_key,
            domain=domain,
            port=port
        )

    def execute(self, request: Request) -> dict:
        result: dict = self.subject_client.post(asdict(request))
        return result
