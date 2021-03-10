# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Service(ABC):
    """The best class of all services"""

    @abstractmethod
    def __init__(self, api_key: str):
        self._api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    @abstractmethod
    def get_available_functions(self):
        pass
