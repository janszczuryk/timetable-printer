class Lesson:
    lesson_id: int
    duration: int
    group_name: str
    lesson_name: str
    lesson_type: str
    room: str | None

    def __init__(self, lesson_id: int, duration: int, group_name: str, lesson_name: str, lesson_type: str,
                 room: str | None) -> None:
        self.lesson_id = lesson_id
        self.duration = duration
        self.group_name = group_name
        self.lesson_name = lesson_name
        self.lesson_type = lesson_type
        self.room = room
