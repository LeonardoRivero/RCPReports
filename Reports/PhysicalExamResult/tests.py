from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from rest_framework import status
from .models import PhysicalExamResults
from faker import Faker
from faker.providers import DynamicProvider
import inspect
# Create your tests here.
physical_exam = DynamicProvider(
     provider_name="physical_exam",
     elements=["Manos", "Pies", "Cabeza", "Pulmones", "Ojos","Pulso","Corazon",
               "Piernas","Columna"],
)
class ExamResultTestCase(TestCase):
    fake = Faker(["es_CO"])
    fake.seed_instance(4321)
    fake.add_provider(physical_exam)

    @property
    def url_physicalexamresult_all(self):
        return f"/api/physicalexamresult/all/"

    @property
    def all_physicalexamresult(self) -> list:
        return self.all_physicalexamresult

    @all_physicalexamresult.setter
    def all_physicalexamresult(self, value):
        self.all_physicalexamresult = value

    @classmethod
    def setUpTestData(self):
        pathology=[]
        for _ in range(5):
            pathology.append({"description":self.fake.physical_exam(),"result":"Normal"})
        for _ in range(5):
            created = PhysicalExamResults.objects.create(date_exam=datetime.now(),
                                                     patient_id= self.fake.pyint(),
                                                     result=pathology)

    def setUp(self):
        pass

    def test_create_exam_result(self):
        print(inspect.currentframe().f_code.co_name)
        pathology = [{"description":"Manos","result":"Normal"},
                     {"description":"Pies","result":"Normales"}]

        # created = PhysicalExamResults.objects.create(date_exam=datetime.now(),
        #                                              patient_id=45,
        #                                              result=pathology)
        url = self.url_physicalexamresult_all
        data={"date_exam": timezone.now(),"patient_id": '45', "result": pathology}
        response = self.client.post(url, data,content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_all_exam_result(self):
        print(inspect.currentframe().f_code.co_name)
        url = self.url_physicalexamresult_all
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        return response.json()
    
    def test_get_by_patient_id(self, pk=1):
        self.test_create_exam_result()
        print(inspect.currentframe().f_code.co_name)
        url = self.url_physicalexamresult_all
        response = self.client.get(f"{url}?patient_id=45")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_all(self):
        all_items=self.test_get_all_exam_result()
        for item in all_items:
            print(inspect.currentframe().f_code.co_name)
            url = self.url_physicalexamresult_all
            self.client.delete(f"{url}{item['_id']}")
