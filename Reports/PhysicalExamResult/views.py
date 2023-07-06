from http import HTTPStatus
from django.http import HttpResponseBadRequest
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from .serializers import PhysicalExamResultSerializer
from .Domine.Interfaces import Controller
from .models import PhysicalExamResults
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response
from .Adapters.Controllers import FactoryController, Controllers
from rest_framework.permissions import IsAuthenticated

class CRUDPhysicalExamResult(GenericAPIView):
    """
    Create,Retrieve,Update or Delete an object Consult.
    """
    # permission_classes = [IsAuthenticated]
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
            response = self.get_serializer(data)
            return Response(response.data, status=status)
        except ValidationError as e:
            return Response(e.detail, status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)
        except AssertionError as e:
            return Response(e, status=HTTPStatus.CONFLICT, exception=True)

    def delete(self, request: Request, pk: int=None):
        try:
            assert pk!=None,"Not Found identifier"
            response, status = self.controller.delete(pk)
            return Response(response, status=status)
        except AssertionError as e:
            return HttpResponseBadRequest(e.args,exception=True)
