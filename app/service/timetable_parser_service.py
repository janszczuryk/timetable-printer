import re
from bs4 import BeautifulSoup

from app.model import TimeTable, Lesson, LessonDescription, WeekRow
from app.model.enum import LessonType


class TimeTableParserService:
    content: bytes
    row_index: int
    row_queue: list[Lesson]

    def __init__(self, content: bytes):
        self.content = content

    def parse_timetable(self, timetable_id: str) -> TimeTable:
        soup = BeautifulSoup(self.content, "html.parser")

        table = soup.find("table", {"id": timetable_id})

        if table is None:
            raise Exception(f"Table with id: {timetable_id} not found")

        teacher = table.find("thead").find("tr").find("th").text

        timetable = TimeTable(timetable_id, teacher)

        for row_index, row in enumerate(table.find("tbody").find_all("tr")):

            self.begin_row(row_index)

            for column_index, column in enumerate(row.find_all("td")):
                if not column.has_attr("class"):
                    continue

                class_ = column["class"].pop()

                if "notAvailable" in class_ or "empty" in class_:
                    lesson = Lesson("", LessonType.OTHER, row_index, 1,
                                    LessonDescription(None, column.text.strip(), None, None))
                elif re.match("c_[0-9]+", class_):
                    lesson = Lesson(
                        class_,
                        LessonType.LESSON,
                        row_index,
                        int(column["rowspan"]),
                        LessonDescription(
                            column.find("div", {"class": "line1"}).text.strip(),
                            column.find("div", {"class": "line2"}).find("span", {"class": "subject"}).text.strip(),
                            column.find("div", {"class": "line2"}).find("span", {"class": "activitytag"}).text.strip(),
                            column.find("div", {"class": "line3"}).text.strip() if column.find("div", {
                                "class": "line3"}) is not None else ""
                        )
                    )
                else:
                    continue

                self.row_add_lesson(lesson)

            self.commit_row(timetable)

        return timetable

    def is_lesson_ended(self, lesson: Lesson) -> bool:
        return self.row_index >= lesson.start_index + lesson.duration_index

    def begin_row(self, row_index) -> None:
        self.row_index = row_index
        self.row_queue = []

    def row_add_lesson(self, lesson: Lesson) -> None:
        self.row_queue.append(lesson)

    def commit_row(self, timetable: TimeTable) -> None:
        if len(self.row_queue) == 0:
            return

        new_lessons_row = []

        if self.row_index == 0:
            new_lessons_row = self.row_queue.copy()
        else:
            self.row_queue.reverse()
            for last_row_lesson in timetable.get_last_row_lessons_table_ordered():
                if self.is_lesson_ended(last_row_lesson):
                    new_lesson = self.row_queue.pop()
                else:
                    # NOTE: Spanner Lesson has to consist start_index and duration_index (decremented, one by row)
                    new_lesson = Lesson.create_spanner(self.row_index, last_row_lesson.duration_index - 1)
                new_lessons_row.append(new_lesson)

        new_row_week_a = []
        new_row_week_b = []

        for new_lesson_index, new_lesson in enumerate(new_lessons_row):
            if new_lesson_index % 2 == 0:
                new_row_week_a.append(new_lesson)
            else:
                new_row_week_b.append(new_lesson)

        timetable.week_a.add_row(WeekRow.create_week_row(self.row_index, new_row_week_a))
        timetable.week_b.add_row(WeekRow.create_week_row(self.row_index, new_row_week_b))

        self.row_queue = []
