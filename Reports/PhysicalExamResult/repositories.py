from datetime import datetime
from typing import Iterable
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import ProtectedError,QuerySet
from .Domine.Entities import PhysicalExamResultEntity
from .Domine.Interfaces import Repository
from .models import PhysicalExamResults
from bson.objectid import ObjectId


class PhisycalExamParameterResultRepository(Repository):

    def add(self, entity: PhysicalExamResultEntity):
        response, created = PhysicalExamResults.objects.get_or_create(
            date_exam=entity.date_exam,
            patient_id=entity.patient_id,
            result=entity.result
        )
        return response

    def get_by_id(self, pk: int) -> QuerySet:
        try:
            objInstance = ObjectId(pk)
            return PhysicalExamResults.objects.get(_id=objInstance)
            # return PhysicalExamResults.objects.filter(patient_id=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get_all(self):
        try:
            return PhysicalExamResults.objects.all()
        except ObjectDoesNotExist:
            raise Http404

    def update(self, entity: PhysicalExamResultEntity, pk: int) -> PhysicalExamResultEntity:
        assert pk==entity._id
        current_record = self.get_by_id(pk)
        current_record.date_exam=entity.date_exam
        current_record.result=entity.result
        current_record.save()
        updated_record = self.get_by_id(pk)
        return updated_record

    def update_partial(self, entity: dict, pk: int):
        raise NotImplementedError()

    def delete(self, id: int) -> bool:
        try:
            response = self.get_by_id(id)
            response.delete()
            return True
        except ProtectedError:
            return False

    def find_by_parameter(self, parameters: dict) -> Iterable[PhysicalExamResultEntity]:
        data = PhysicalExamResults.objects.filter(**parameters)
        if (data.exists()):
            return data
        return None
