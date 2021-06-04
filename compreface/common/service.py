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

from abc import ABC, abstractmethod
from compreface.common.typed_dict import AllOptionsDict


class Service(ABC):
    """The best class of all services"""

    @abstractmethod
    def __init__(self, api_key: str, options: AllOptionsDict):
        self._api_key = api_key
        self._options = options

    @property
    def api_key(self):
        return self._api_key

    @property
    def options(self):
        return self._options

    @abstractmethod
    def get_available_functions(self):
        pass
