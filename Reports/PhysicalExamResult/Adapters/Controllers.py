from __future__ import annotations
from typing import Tuple
from rest_framework.request import Request
from http import HTTPStatus
from ..Domine.Entities import PhysicalExamResultEntity
from ..repositories import PhisycalExamParameterResultRepository
# from  RCP_Project.containers import container
from ..Aplication.UseCases import PhysicalExamResultUseCase
from ..Domine.Interfaces import Repository, Controller
from enum import Enum
from django.db.models import QuerySet
from http import HTTPStatus
# from dependency_injector.wiring import inject


class Controllers(Enum):
    PhysicalExamResult = 1


class FactoryController():
    @staticmethod
    def create_controller(controller: Enum):
        all_controllers = {
            "PhysicalExamResult": PhysicalExamResultController(),
        }
        return all_controllers[controller.name]


class PhysicalExamResultController(Controller):
    def __init__(self) -> None:
        self.repository = PhisycalExamParameterResultRepository()
        self.use_case = PhysicalExamResultUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[QuerySet, HTTPStatus]:
        try:
            if (request.query_params):
                data = self.use_case.get_by_query_params(request.query_params)
                status = HTTPStatus.NO_CONTENT if data == None else HTTPStatus.OK
                return (data, status)
            if pk:
                data = self.use_case.get_by_id(pk)
                return (data, HTTPStatus.ACCEPTED)
            else:
                data = self.use_case.get_all()
                return (data, HTTPStatus.ACCEPTED)
        except KeyError as e:
            return (None, HTTPStatus.UNPROCESSABLE_ENTITY)

    def post(self, request: Request):
        entity = PhysicalExamResultEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = PhysicalExamResultEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        response = self.use_case.delete(pk)
        status = HTTPStatus.NO_CONTENT if response == True else HTTPStatus.METHOD_NOT_ALLOWED
        return (None, status)

    def patch(self, request: Request, pk: int):
        raise NotImplementedError
