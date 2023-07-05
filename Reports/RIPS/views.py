from datetime import datetime
from http import HTTPStatus
from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.request import Request

from .serializers import PhysicalExamResultSerializer
from .Adapters import Controllers
from .Domine.Interfaces import Controller
from .models import PhysicalExamResults
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response


# Create your views here.


# def index(request):
#     e = PhysicalExamResults()
#     e.date_exam = datetime.today()
#     e.result = [{'description': 'manos', 'result': '56'},
#                 {'description': 'pies', 'result': '66'}]
#     e.patient_id = 89
#     e.save()
#     return HttpResponse()


class CRUDPhysicalExamResult(GenericAPIView):
    """
    Create,Retrieve,Update or Delete an object Consult.
    """
    queryset = PhysicalExamResults.objects.none()
    controller: Controller = None

    def get_serializer_class(self):
        return PhysicalExamResultSerializer

    def get(self, request: Request, pk: int = None):
        try:
            data, status = self.controller.get(request, pk)
            response = self.get_serializer(data, many=True)
            return Response(response.data, status=status)
        except KeyError as e:
            return Response(str(e), status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)

    @extend_schema(
        request=PhysicalExamResultSerializer,
    )
    def post(self, request: Request, ):
        data, status = self.controller.post(request)
        response = model_to_dict(data)
        return Response(response, status=status)

    def put(self, request: Request, pk: int):
        try:
            data, status = self.controller.put(request, pk)
            response = model_to_dict(data)
            return Response(response, status=status)
        except ValidationError as e:
            return Response(e.detail, status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)
