class LessonDescription:
    group_name: str | None
    lesson_name: str
    lesson_type: str | None
    room: str | None

    def __init__(self, group_name: str | None, lesson_name: str, lesson_type: str | None, room: str | None):
        self.group_name = group_name
        self.lesson_name = lesson_name
        self.lesson_type = lesson_type
        self.room = room

    def __str__(self) -> str:
        return f'{self.group_name or ""} {self.lesson_name or ""} {self.lesson_type} {self.room or ""}'
