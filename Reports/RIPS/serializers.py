# from rest_framework import serializers


# class ExamResult(serializers.Serializer):
#     description = serializers.CharField(max_length=100)
#     result = serializers.CharField(max_length=100)


# class PhysicalExamResultSerializer(serializers.Serializer):
#     _id = serializers.IntegerField()
#     date_exam = serializers.DateTimeField()
#     patient_id = serializers.IntegerField()
#     result = serializers.ListField(
#         child=serializers.ListField(child=ExamResult())
#     )
