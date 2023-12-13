from app.model.enum import LessonType
from app.model.lesson_description import LessonDescription
from app.service import TimeService


class Lesson:
    lesson_id: str
    type: LessonType
    start_index: int
    duration_index: int
    description: LessonDescription | None

    def __init__(self,
                 lesson_id: str,
                 type: LessonType,
                 start_index: int,
                 duration_index: int,
                 description: LessonDescription | None = None
                 ):
        self.lesson_id = lesson_id
        self.type = type
        self.start_index = start_index
        self.duration_index = duration_index
        self.description = description

    @staticmethod
    def create_spanner(row_index: int):
        return Lesson("span", LessonType.SPANNER, row_index, 1, None)

    def print(self) -> None:
        hour = TimeService.get_hour_by_row_index(self.start_index)
        match self.type:
            case LessonType.LESSON:
                duration = TimeService.get_minutes_by_row_index(self.duration_index)
                if self.description is None:
                    raise RuntimeError("Lesson description not defined")
                print(f"[{hour}] [{duration} min] {self.description.group_name} {self.description.lesson_name} {self.description.lesson_type} {self.description.room}")
            case LessonType.SPANNER:
                print(f"[{hour}] Spanner")
            case LessonType.OTHER:
                if self.description is None:
                    raise RuntimeError("Lesson description not defined")
                print(f"[{hour}] {self.description.lesson_name}")
