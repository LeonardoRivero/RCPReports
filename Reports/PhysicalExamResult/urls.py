from django.urls import path, re_path
from .views import CRUDPhysicalExamResult
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("physicalexamresult/all/", CRUDPhysicalExamResult.as_view()),
    re_path('physicalexamresult/(?P<pk>[0-9a-f-]+)/', CRUDPhysicalExamResult.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
