from datetime import date, timedelta, timezone
from typing import Iterable
from ..Domine.Interfaces import Controller, UseCase


class PhysicalExamResultUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)

    def get_by_query_params(self, data: dict):
        if ('patient_id' in data):
            return self.get_result_by_patient_id(int(data['patient_id']))
        raise KeyError("Query params not valid")

    def get_result_by_patient_id(self, patient_id: int):
        return self.repository.find_by_parameter({'patient_id': patient_id})
