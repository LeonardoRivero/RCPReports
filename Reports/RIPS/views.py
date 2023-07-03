from http import HTTPStatus
from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.request import Request
from .Adapters import Controllers
from .Domine.Interfaces import Controller
from .models import Blog
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.response import Response

# Create your views here.


def index(request):
    e = Blog()
    e.name = "Gaby"
    e.last_name = "Rojas"
    e.save()
    return HttpResponse()


class CRUDAppointment(GenericAPIView):
    """
    Create,Retrieve,Update or Delete an object Consult.
    """
    queryset = Blog.objects.none()
    controller: Controller = Controllers.FactoryController.create_controller(
        Controllers.Appointment)

    def get_serializer_class(self):
        return AppointmentSerializer

    @extend_schema(
        responses=AppointmentSerializer,
    )
    def get(self, request: Request, pk: int = None):
        try:
            data, status = self.controller.get(request, pk)
            response = self.get_serializer(data, many=True)
            return Response(response.data, status=status)
        except KeyError as e:
            return Response(str(e), status=HTTPStatus.UNPROCESSABLE_ENTITY, exception=True)

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
