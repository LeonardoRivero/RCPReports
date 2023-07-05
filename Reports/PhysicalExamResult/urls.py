from django.urls import path
from .views import CRUDPhysicalExamResult
from django.contrib import admin


urlpatterns = [
    path("physicalexamresult/", CRUDPhysicalExamResult.as_view()),
]
