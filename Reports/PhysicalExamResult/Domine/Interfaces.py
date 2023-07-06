from abc import ABC, ABCMeta, abstractmethod
from typing import Tuple
from requests import Request
from django.db.models import QuerySet
from http import HTTPStatus


class Repository(ABC):
    @abstractmethod
    def add(self, entity: object):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, ):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: object, pk: int) -> object:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def find_by_parameter(self, parameters: dict):
        raise NotImplementedError

    @abstractmethod
    def update_partial(self, entity: dict, pk: int):
        raise NotImplementedError


class Controller(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_repository(self) -> Repository:
        raise NotImplementedError

    @abstractmethod
    def get(self, request: Request, pk: int = None) -> Tuple[QuerySet, HTTPStatus]:
        raise NotImplementedError

    @abstractmethod
    def post(self, request: Request):
        raise NotImplementedError

    @abstractmethod
    def put(self, request: Request, pk: int = None):
        raise NotImplementedError

    @abstractmethod
    def patch(self, request: Request, pk: int = None):
        raise NotImplementedError

    @abstractmethod
    def delete(self, pk: int = None):
        raise NotImplementedError


class UseCase(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, controller: Controller) -> None:
        super().__init__()
        self.controller = controller
        self.repository = controller.get_repository()

    def update(self, entity: dict, pk: int):
        return self.repository.update(entity, pk)

    def create(self, entity: dict):
        return self.repository.add(entity)

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)

    def get_all(self):
        return self.repository.get_all()

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)

    def update_partial(self, entity: dict, pk: int):
        return self.repository.update_partial(entity, pk)
