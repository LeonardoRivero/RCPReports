from datetime import datetime
from rest_framework.exceptions import ValidationError
from typing import Iterable
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import ProtectedError
from .Domine.Entities import PhysicalExamResultEntity
from .Domine.Interfaces import Repository
from .models import PhysicalExamResults
from bson.objectid import ObjectId


class PhisycalExamParameterResultRepository(Repository):

    def add(self, entity: PhysicalExamResultEntity):
        # model=PhysicalExamResults()
        # model.date_exam=entity.date_exam
        # model.patient_id=entity.patient_id
        # model.result=entity.result
        # model.save()
        # e = PhysicalExamResults()
        # e.date_exam = entity.date_exam
        # e.result = entity.result
        # e.patient_id = entity.patient_id
        # response=e.save()
        # print(response)
        response, created = PhysicalExamResults.objects.get_or_create(
            date_exam=entity.date_exam,
            patient_id=entity.patient_id,
            result=entity.result
        )
        return response

    def get_by_id(self, pk: int) -> Iterable[PhysicalExamResults]:
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
        current_record = self.get_by_id(pk)
        return current_record.update_or_create(
            date_exam=datetime.today(),
            patient_id=entity.patient_id,
            result=entity.result
        )

        # entity_as_dict = asdict(entity)
        # serializer = self.SaverSerializer(current_record, data=entity_as_dict)
        # if serializer.is_valid():
        #     record = serializer.save()
        #     return record
        # raise ValidationError(serializer.errors)

    def update_partial(self, entity: dict, pk: int):
        raise NotImplementedError()
        current_record = self.get_by_id(pk)
        serializer = self.SaverSerializer(current_record, data=entity, partial=True)
        if serializer.is_valid():
            record = serializer.save()
            return record
        raise ValidationError(serializer.errors)

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
