# Create your models here.
from djongo import models


class PhysicalExamResults(models.Model):
    _id = models.ObjectIdField()
    date_exam = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    patient_id = models.ObjectIdField()

    objects = models.DjongoManager()
