from django.urls import path, re_path
from .views import CRUDPhysicalExamResult
from django.contrib import admin


urlpatterns = [
    path("physicalexamresult/all/", CRUDPhysicalExamResult.as_view()),
    re_path('physicalexamresult/(?P<pk>[0-9a-f-]+)/', CRUDPhysicalExamResult.as_view()),
    # path('physicalexamresult/<int:patient_id>/', CRUDPhysicalExamResult.as_view()),
]
