from dataclasses import InitVar, dataclass, field
from typing import List
import datetime


@dataclass
class ExamResult:
    result: str
    description: str


@dataclass
class PhysicalExamResultEntity():
    date_exam: datetime
    result: List[ExamResult]
    patient_id: int = 0
    _id: int = 0


# @dataclass
# class PaymentOptionsEntity (BaseEntity):
#     pass


# @dataclass
# class SpecialityEntity(BaseEntity):
#     pass


# @dataclass
# class RelationCodeEntity:
#     description: str
#     code: str
#     dxmaincode: int
#     id: int = 0


# @dataclass
# class ReasonConsultEntity:
#     abbreviation: str
#     id: int = 0


# @dataclass
# class DXMainCodeEntity:
#     CUP: str
#     description: str
#     speciality: int = 0
#     id: int = 0


# @dataclass
# class DoctorEntity:
#     codigo: str
#     name: str
#     lastName: str
#     id: int = 0


# @dataclass
# class ScheduleEntity:
#     title: str
#     start: datetime
#     end: datetime
#     patient: int
#     speciality: int
#     doctor: int
#     observations: int
#     id: int = 0


# @dataclass
# class AppointmentEntity:
#     price: float
#     copayment: float
#     amountPaid: float
#     date: datetime
#     authorizationNumber: str
#     patientStatus: int
#     reasonConsult: int
#     patient: int
#     doctor: int
#     schedule: int
#     paymentMethod: int
#     codeTransaction: str
#     id: int = 0
