# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class ClientRequest(ABC):
    """The best class of all requests"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass
