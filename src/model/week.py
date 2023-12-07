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

    def get_all_days(self):
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]
