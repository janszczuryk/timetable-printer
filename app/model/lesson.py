from .enum import LessonType
from .lesson_description import LessonDescription
from app.service import TimeService


class Lesson:
    lesson_id: str
    lesson_type: LessonType
    start_index: int
    duration_index: int
    description: LessonDescription | None

    def __init__(self,
                 lesson_id: str,
                 lesson_type: LessonType,
                 start_index: int,
                 duration_index: int,
                 description: LessonDescription | None = None
                 ):
        self.lesson_id = lesson_id
        self.lesson_type = lesson_type
        self.start_index = start_index
        self.duration_index = duration_index
        self.description = description

    @staticmethod
    def create_spanner(start_index: int, duration_index: int):
        return Lesson("spanner", LessonType.SPANNER, start_index, duration_index, None)

    def print(self) -> None:
        match self.lesson_type:
            case LessonType.LESSON:
                duration = TimeService.get_minutes_by_row_index(self.duration_index)
                if self.description is None:
                    raise RuntimeError("Lesson description not defined")
                print(
                    f"[{duration} min] {self.description.group_name} {self.description.lesson_name} {self.description.lesson_type} {self.description.room}",
                    end="")
            case LessonType.SPANNER:
                print(f"Spanner", end="")
            case LessonType.OTHER:
                if self.description is None:
                    raise RuntimeError("Lesson description not defined")
                print(f"{self.description.lesson_name}", end="")
