from django.urls import path

from .views import CRUDPhysicalExamResult


urlpatterns = [
    path("physicalexamresult/", CRUDPhysicalExamResult.as_view()),
]
