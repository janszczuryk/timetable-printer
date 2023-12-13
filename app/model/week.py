from .lesson import Lesson
from .enum import WeekDayType


class Week:
    monday: list[Lesson]
    tuesday: list[Lesson]
    wednesday: list[Lesson]
    thursday: list[Lesson]
    friday: list[Lesson]

    def __init__(self):
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []

    def print(self):
        for day_index, day in enumerate(self.get_all_days()):
            print(f"Day: {WeekDayType(day_index).name}")
            for lesson in day:
                lesson.print()

    def get_all_days(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]


