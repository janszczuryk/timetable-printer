from src.service import TimeService


class Lesson:
    lesson_id: str
    start_index: int
    duration_index: int
    group_name: str
    lesson_name: str
    lesson_type: str
    room: str | None

    def __init__(self,
                 lesson_id: str,
                 start_index: int,
                 duration_index: int,
                 group_name: str,
                 lesson_name: str,
                 lesson_type: str,
                 room: str | None) -> None:
        self.lesson_id = lesson_id
        self.start_index = start_index
        self.duration_index = duration_index
        self.group_name = group_name
        self.lesson_name = lesson_name
        self.lesson_type = lesson_type
        self.room = room

    def print(self) -> None:
        duration = f"[{TimeService.get_minutes_by_row_index(self.duration_index)} min]" if self.duration_index > 1 else ""
        print(
            f"[{TimeService.get_hour_by_row_index(self.start_index)}] {duration} {self.group_name} {self.lesson_name} {self.lesson_type} {self.room}")
