from datetime import date, timedelta, timezone
from typing import Iterable
from ..Domine.Interfaces import Controller, UseCase



class PhysicalExamResultUseCase(UseCase):

    def __init__(self, controller: Controller):
        super().__init__(controller)
