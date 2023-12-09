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

    def get_week_days_index_ordered(self):
        return [
            self.week_a.monday,
            self.week_b.monday,
            self.week_a.tuesday,
            self.week_b.tuesday,
            self.week_a.wednesday,
            self.week_b.wednesday,
            self.week_a.thursday,
            self.week_b.thursday,
            self.week_a.friday,
            self.week_b.friday,
        ]

    def print(self):
        print(f"Timetable:  {self.timetable_id}")
        print(f"Teacher:  {self.teacher}")
        print("Week A:")
        self.week_a.print()
        print("Week B:")
        self.week_b.print()