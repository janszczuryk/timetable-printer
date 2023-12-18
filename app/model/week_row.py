from .lesson import Lesson
from app.service import TimeService


class WeekRow:
    row_index: int
    monday: Lesson
    tuesday: Lesson
    wednesday: Lesson
    thursday: Lesson
    friday: Lesson

    def __init__(self, row_index: int, monday: Lesson, tuesday: Lesson, wednesday: Lesson, thursday: Lesson,
                 friday: Lesson):
        self.row_index = row_index
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

    def __str__(self) -> str:
        hour = TimeService.get_hour_by_row_index(self.row_index)
        all_lessons = self.get_all_lessons()
        return '\t'.join(list(map(lambda item: str(item), [hour, *all_lessons])))

    def get_all_lessons(self) -> list[Lesson]:
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

    def get_hour_start(self) -> str:
        return TimeService.get_hour_by_row_index(self.row_index)

    def get_hour_end(self) -> str:
        return TimeService.get_hour_by_row_index(self.row_index + 1)

    @staticmethod
    def create_week_row(row_index: int, lessons: list[Lesson]):
        return WeekRow(row_index, *lessons)
