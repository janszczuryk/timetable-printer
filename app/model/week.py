from enum import StrEnum, IntEnum
from .lesson import Lesson


class Week:
    monday: list[Lesson]
    tuesday: list[Lesson]
    wednesday: list[Lesson]
    thursday: list[Lesson]
    friday: list[Lesson]

    def __init__(self):
        self.monday = list()
        self.tuesday = list()
        self.wednesday = list()
        self.thursday = list()
        self.friday = list()

    def print(self):
        for day_index, day in enumerate(self.get_all_days()):
            print(f"Day: {WeekDayType(day_index).name}")
            for lesson in day:
                lesson.print()

    def get_all_days(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]


class WeekType(StrEnum):
    A = 'a'
    B = 'b'


class WeekDayType(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
