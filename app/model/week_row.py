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

    def print(self) -> None:
        hour = TimeService.get_hour_by_row_index(self.row_index)
        print(f"[{hour}]", end="")
        for lesson in self.get_all_lessons():
            print("\t", end="")
            lesson.print()
        print("")

    def get_all_lessons(self) -> list[Lesson]:
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday]

    def get_hour(self) -> str:
        start_hour = TimeService.get_hour_by_row_index(self.row_index)
        end_hour = TimeService.get_hour_by_row_index(self.row_index + 1)
        return f"{start_hour} &mdash; {end_hour}"

    @staticmethod
    def create_week_row(row_index: int, lessons: list[Lesson]):
        return WeekRow(row_index, *lessons)
