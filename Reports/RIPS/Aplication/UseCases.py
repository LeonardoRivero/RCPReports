from datetime import date, timedelta, timezone
from typing import Iterable
from ..Domine.Entities import ScheduleEntity
from ..Domine.Interfaces import Repository, Controller, UseCase


class SpecialityUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
        self.controller = controller
        self.repository = controller.get_repository()

    def get_by_query_params(self, data: dict):
        if ('doctorId' in data):
            return self.get_speciality_by_doctor_id(int(data['doctorId']))
        raise KeyError("Query params not valid")

    def get_speciality_by_doctor_id(self, doctor_id: int):
        return self.repository.find_by_parameter({'doctor': doctor_id})



class PatientStatusUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)


class MedicalHistoryUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)


class DxMainCodeUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
        self.controller = controller
        self.repository = controller.get_repository()

    def get_by_query_params(self, data: dict):
        if ('speciality' in data):
            return self.get_by_speciality_id(int(data['speciality']))
        raise KeyError("Query params not valid")

    def get_by_speciality_id(self, speciality_id: int):
        return self.repository.find_by_parameter({'speciality': speciality_id})


class ReasonConsultUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)


class PaymentOptionsUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)


class RelationCodeUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
        self.controller = controller
        self.repository = controller.get_repository()

    def get_by_query_params(self, data: dict):
        if ('dxMainCodeId' in data):
            return self.get_by_dxmain_code_id(int(data['dxMainCodeId']))
        raise KeyError("Query params not valid")

    def get_by_dxmain_code_id(self, id: int):
        return self.repository.find_by_parameter({'dxmaincode': id})


class DoctorUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
        self.controller = controller
        self.repository = controller.get_repository()

    def get_by_query_params(self, data: dict):
        if ('speciality' in data):
            return self.get_by_speciality_id(int(data['speciality']))
        raise KeyError("Query params not valid")

    def get_by_speciality_id(self, id: int):
        return self.repository.find_by_parameter({'speciality': id})


class AppointmentUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)

    def get_by_query_params(self, data: dict):
        if ('patientId' in data):
            return self.get_appointment_by_patient_id(int(data['patientId']))
        raise KeyError("Query params not valid")

    def get_appointment_by_patient_id(self, id: int):
        return self.repository.find_by_parameter({'patientId': id})

class ScheduleUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
        self.controller = controller
        self.repository = controller.get_repository()

    def get_by_query_params(self, data: dict):
        if ('start' in data and "doctor" in data):
            return self.has_doctor_available(data['start'],int(data['doctor']))
        if ('start' in data and 'end' in data):
            return self.get_events_by_range(data['start'],data['end'])
        if ('patientIdentification' in data):
            return self.get_by_patient_identification('patientIdentification')
        raise KeyError("Query params not valid")

    def has_doctor_available(self, start: str, doctor_id: int) -> bool:
        data= self.repository.find_by_parameter({'start': start,'doctor_id':doctor_id})
        response = True if data == None else False
        return response

    def get_events_by_range(self, start: str, end: str)->Iterable[ScheduleEntity]:
        response=self.repository.find_by_parameter({'end__lte': start,'start__gte':end})
        return response

    def get_by_patient_identification(self, patient_identification: str):
        now = timezone.now()
        tomorrow = date.today() + timedelta(1)
        return self.repository.find_by_parameter({'patient__identification': patient_identification,'start__gte':now,'end__lt':tomorrow})

        # exist = Schedule.objects.filter(
        #     patient__identification=patient_identification, start__gte=now, end__lt=tomorrow).exists()
        # if (exist):
        #     data = Schedule.objects.filter(
        #         patient__identification=patient_identification, start__gte=now, end__lte=tomorrow)
        #     serializer = RelationScheduleSerializer(data, many=True)
        #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # serializer = RelationScheduleSerializer(None, many=False)
        # return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)