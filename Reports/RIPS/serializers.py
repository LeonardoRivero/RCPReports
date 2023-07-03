from rest_framework import serializers
from .models import PhysicalExamResults


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalExamResults
        fields = '__all__'
