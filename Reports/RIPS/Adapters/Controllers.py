from __future__ import annotations
from typing import Tuple
from rest_framework.request import Request
from http import HTTPStatus
from  RCP_Project.containers import container
from ..Domine.Entities import AppointmentEntity, DXMainCodeEntity, DoctorEntity, PatientStatusEntity, PaymentOptionsEntity, ReasonConsultEntity, RelationCodeEntity, ScheduleEntity, SpecialityEntity
from ..Aplication.UseCases import AppointmentUseCase, DoctorUseCase, DxMainCodeUseCase, PatientStatusUseCase, PaymentOptionsUseCase, ReasonConsultUseCase, RelationCodeUseCase, ScheduleUseCase, SpecialityUseCase
from ..Domine.Interfaces import Repository, Controller
from enum import Enum
from dependency_injector.wiring import inject

class Controllers(Enum):
    Speciality = 1     
    DxMainCode = 2
    PatientStatus=3
    ReasonConsult=4
    PaymentOptions=5
    RelationCode=6
    Doctor=7
    Appointment=8
    Schedule=9

class FactoryController():
    @staticmethod
    def create_controller(controller:Enum):
        all_controllers={
            "Speciality":SpecialityController(),
            "DxMainCode":DxMainCodeController(),
            "PatientStatus":PatientStatusController(),
            "ReasonConsult":ReasonConsultController(),
            "PaymentOptions":PaymentOptionsController(),
            "RelationCode":RelationCodeController(),
            "Doctor":DoctorController(),
            "Appointment":AppointmentController(),
            "Schedule":ScheduleController()
        }
        return all_controllers[controller.name]

@inject
class SpecialityController(Controller):
    def __init__(self,repository:Repository=container.repositories("speciality")) -> None:
        self.repository=repository
        self.use_case = SpecialityUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
        use_case = SpecialityUseCase(self)
        try:
            if (request.query_params):
                data = use_case.get_by_query_params(request.query_params)
                status = HTTPStatus.NO_CONTENT if data == None else HTTPStatus.OK
                return (data, status)
            if pk:
                data = use_case.get_by_id(pk)
                return (data, HTTPStatus.ACCEPTED)
            else:
                data = use_case.get_all()
                return (data, HTTPStatus.ACCEPTED)
        except KeyError as e:
            return (None, HTTPStatus.UNPROCESSABLE_ENTITY)

    def post(self, request: Request):
        entity = SpecialityEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = SpecialityEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class DxMainCodeController(Controller):
    def __init__(self,repository:Repository=container.repositories("dx_main_code")) -> None:
        self.repository=repository
        self.use_case = DxMainCodeUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
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
        entity = DXMainCodeEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = DXMainCodeEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class PatientStatusController(Controller):
    def __init__(self,repository:Repository=container.repositories("patient_status")) -> None:
        self.repository=repository
        self.use_case = PatientStatusUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
        try:
            if pk:
                data = self.use_case.get_by_id(pk)
                return (data, HTTPStatus.ACCEPTED)
            else:
                data = self.use_case.get_all()
                return (data, HTTPStatus.ACCEPTED)
        except KeyError as e:
            return (None, HTTPStatus.UNPROCESSABLE_ENTITY)

    def post(self, request: Request):
        entity = PatientStatusEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        raise NotImplementedError

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class ReasonConsultController(Controller):
    def __init__(self,repository:Repository=container.repositories("reason_consult")) -> None:
        self.repository=repository
        self.use_case = ReasonConsultUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
        try:
            if pk:
                data = self.use_case.get_by_id(pk)
                return (data, HTTPStatus.ACCEPTED)
            else:
                data = self.use_case.get_all()
                return (data, HTTPStatus.ACCEPTED)
        except KeyError as e:
            return (None, HTTPStatus.UNPROCESSABLE_ENTITY)

    def post(self, request: Request):
        entity = ReasonConsultEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        raise NotImplementedError

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class PaymentOptionsController(Controller):
    def __init__(self,repository:Repository=container.repositories("payment_options")) -> None:
        self.repository=repository
        self.use_case = PaymentOptionsUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
        try:
            if pk:
                data = self.use_case.get_by_id(pk)
                return (data, HTTPStatus.ACCEPTED)
            else:
                data = self.use_case.get_all()
                return (data, HTTPStatus.ACCEPTED)
        except KeyError as e:
            return (None, HTTPStatus.UNPROCESSABLE_ENTITY)

    def post(self, request: Request):
        entity = PaymentOptionsEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        raise NotImplementedError

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class RelationCodeController(Controller):
    def __init__(self,repository:Repository=container.repositories("relation_code")) -> None:
        self.repository=repository
        self.use_case = RelationCodeUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]: # type: ignore
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
        entity = RelationCodeEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = RelationCodeEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class DoctorController(Controller):
    def __init__(self,repository:Repository=container.repositories("doctor")) -> None:
        self.repository=repository
        self.use_case = DoctorUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
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
        entity = DoctorEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = DoctorEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class AppointmentController(Controller):
    def __init__(self,repository:Repository=container.repositories("appointment")) -> None:
        self.repository=repository
        self.use_case = AppointmentUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
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
        entity = AppointmentEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = AppointmentEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError

@inject
class ScheduleController(Controller):
    def __init__(self,repository:Repository=container.repositories("schedule")) -> None:
        self.repository=repository
        self.use_case = ScheduleUseCase(self)

    def get_repository(self) -> Repository:
        return self.repository

    def get(self, request: Request, pk: int = None) -> Tuple[object, HTTPStatus]:
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
        start: str = request.data["start"]
        doctor: int = int(request.data["doctor"])
        doctor_available=self.use_case.has_doctor_available(start,doctor)
        if (doctor_available is False):
            raise AssertionError ('Doctor not available')
        entity = ScheduleEntity(**request.data)
        response = self.use_case.create(entity)
        return (response, HTTPStatus.ACCEPTED)

    def put(self, request: Request, pk: int):
        entity = ScheduleEntity(**request.data)
        response = self.use_case.update(entity, pk)
        return (response, HTTPStatus.ACCEPTED)

    def delete(self, pk: int):
        raise NotImplementedError

    def patch(self, request: Request, pk: int):
        raise NotImplementedError
