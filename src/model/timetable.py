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

    def print(self):
        print(f"Timetable:  {self.timetable_id}")
        print(f"Teacher:  {self.teacher}")
        print(f"Week A:")
        for i, day in enumerate(self.week_a.get_all_days(), 1):
            print(f"Day: {i}")
            for lesson in day:
                print(f"- {lesson.duration * 15} min, {lesson.group_name} {lesson.lesson_name} {lesson.lesson_type} {lesson.room}")
        print(f"Week B:")
        for i, day in enumerate(self.week_b.get_all_days(), 1):
            print(f"Day: {i}")
            for lesson in day:
                print(f"- {lesson.duration * 15} min, {lesson.group_name} {lesson.lesson_name} {lesson.lesson_type} {lesson.room}")