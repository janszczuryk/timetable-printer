from .week import Week


class TimeTable:
    timetable_id: str
    teacher: str
    week_a: Week
    week_b: Week

    def __init__(self, timetable_id: str, teacher: str):
        self.timetable_id = timetable_id
        self.teacher = teacher
        self.week_a = Week()
        self.week_b = Week()

    def __str__(self) -> str:
        return f"""\
Timetable: {self.timetable_id}
Teacher: {self.teacher}

Week A:
{str(self.week_a)}

Week B:
{str(self.week_b)}
"""

    def get_last_row_lessons_table_ordered(self):
        week_a_last_row = self.week_a.get_last_row()
        week_b_last_row = self.week_b.get_last_row()
        return [
            week_a_last_row.monday,
            week_b_last_row.monday,
            week_a_last_row.tuesday,
            week_b_last_row.tuesday,
            week_a_last_row.wednesday,
            week_b_last_row.wednesday,
            week_a_last_row.thursday,
            week_b_last_row.thursday,
            week_a_last_row.friday,
            week_b_last_row.friday,
        ]

    def print(self) -> None:
        print(self)
