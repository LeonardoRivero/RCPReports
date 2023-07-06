from http import HTTPStatus
from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from .serializers import PhysicalExamResultSerializer
from .Domine.Interfaces import Controller
from .models import PhysicalExamResults
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from .Adapters.Controllers import FactoryController, Controllers


class CRUDPhysicalExamResult(GenericAPIView):
    """
    Create,Retrieve,Update or Delete an object Consult.
    """
    queryset = PhysicalExamResults.objects.none()
    controller: Controller = FactoryController.create_controller(Controllers.PhysicalExamResult)

    def get_serializer_class(self):
        return PhysicalExamResultSerializer

    def get(self, request: Request, pk: int = None):
        try:
            data, status = self.controller.get(request, pk)
            is_many = True if pk == None else False
            response = PhysicalExamResultSerializer(data, many=is_many)
            return Response(response.data, status=status)
        except (KeyError, TypeError) as e:
            return Response(str(e), status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)

    @extend_schema(
        request=PhysicalExamResultSerializer,
    )
    def post(self, request: Request, ):
        data, status = self.controller.post(request)
        response = PhysicalExamResultSerializer(data)
        return Response(response.data, status=status)

    def put(self, request: Request, pk: int):
        try:
            data, status = self.controller.put(request, pk)
            response = model_to_dict(data)
            return Response(response, status=status)
        except ValidationError as e:
            return Response(e.detail, status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)
