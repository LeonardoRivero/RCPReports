from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from typing import Iterable
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import QuerySet, ProtectedError
from dataclasses import asdict
from .models import PhysicalExamResults


# class PhisycalExamParameterRepository(AbstractRepository):
#     class SaverSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = PhysicalExamResults
#             fields = ["id", "description", "speciality", "active"]

#     def add(self, entity: PhysicalExamParameterEntity):
#         entity_as_dict = asdict(entity)
#         serializer = self.SaverSerializer(data=entity_as_dict)
#         if serializer.is_valid():
#             record = serializer.save()
#             return record
#         raise ValidationError

#     def get_by_id(self, pk: int) -> QuerySet[PhysicalExamResults]:
#         try:
#             return PhysicalExamResults.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             raise Http404

#     def get_all(self):
#         return PhysicalExamResults.objects.all()

#     def update(self, entity: PhysicalExamParameterEntity, pk: int) -> PhysicalExamParameterEntity:
#         current_record = self.get_by_id(pk)
#         entity_as_dict = asdict(entity)
#         serializer = self.SaverSerializer(current_record, data=entity_as_dict)
#         if serializer.is_valid():
#             record = serializer.save()
#             return record
#         raise ValidationError(serializer.errors)

#     def update_partial(self, entity: dict, pk: int):
#         current_record = self.get_by_id(pk)
#         serializer = self.SaverSerializer(current_record, data=entity, partial=True)
#         if serializer.is_valid():
#             record = serializer.save()
#             return record
#         raise ValidationError(serializer.errors)

#     def delete(self, id: int) -> bool:
#         try:
#             response = self.get_by_id(id)
#             response.delete()
#             return True
#         except ProtectedError:
#             return False

#     def find_by_parameter(self, parameters: dict) -> Iterable[PhysicalExamParameterEntity]:
#         data = PhysicalExamResults.objects.filter(**parameters)
#         if (data.exists()):
#             return data
#         return None
