# # Create your models here.
# from djongo import models


# class ExamResult(models.Model):
#     description = models.CharField(max_length=100)
#     result = models.CharField(max_length=100)

#     class Meta:
#         abstract = True


# class PhysicalExamResults(models.Model):
#     _id = models.ObjectIdField()
#     date_exam = models.DateTimeField(auto_now_add=True)
#     patient_id = models.IntegerField()
#     result = models.ArrayField(
#         model_container=ExamResult,
#     )
#     objects = models.DjongoManager()
