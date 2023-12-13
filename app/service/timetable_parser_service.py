import re
from bs4 import BeautifulSoup

from app.model import TimeTable, Lesson, LessonDescription
from app.model.enum import WeekType, WeekDayType, LessonType
from app.service import TimeService


class TimeTableParserService:
    content: bytes
    logging_enabled: bool

    def __init__(self, content: bytes, logging_enabled: bool = False):
        self.content = content
        self.logging_enabled = logging_enabled

    def parse_timetable(self, timetable_id: str) -> TimeTable:
        soup = BeautifulSoup(self.content, "html.parser")

        table = soup.find("table", {"id": timetable_id})

        if table is None:
            raise Exception(f"Table with id: {timetable_id} not found")

        teacher = table.find("thead").find("tr").find("th").text

        timetable = TimeTable(timetable_id, teacher)

        for row_index, row in enumerate(table.find("tbody").find_all("tr")):
            print(f"[{TimeService.get_hour_by_row_index(row_index)}] ---------------") if self.logging_enabled else None

            for column_index, column in enumerate(row.find_all("td")):
                if not column.has_attr("class"):
                    continue

                class_ = column["class"].pop()

                if "notAvailable" in class_ or "empty" in class_:
                    lesson = Lesson("", LessonType.OTHER, row_index, 1, LessonDescription(None, column.text.strip(), None, None))
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

                print(
                    f"{column_index} - Dur: {lesson.duration_index}  {lesson.description.lesson_name}") if self.logging_enabled else None

                (week_type, week_day_type) = self._determine_weekday(timetable, row_index)

                self._add_lesson(timetable, lesson, week_type, week_day_type)

        return timetable

    def _determine_weekday(self, timetable: TimeTable, row_index: int) -> (WeekType, WeekDayType):
        def has_day_free_slot(day: list[Lesson]) -> bool:
            if len(day) == 0:
                return True

            last_lesson = day[-1]
            return row_index >= last_lesson.start_index + last_lesson.duration_index

        free_slots_row = list(map(has_day_free_slot, timetable.get_week_days_index_ordered()))
        free_slot_index = free_slots_row.index(True)

        week_type = WeekType.A if free_slot_index % 2 == 0 else WeekType.B
        week_day_type = WeekDayType(free_slot_index // 2)

        return week_type, week_day_type

    def _add_lesson(self, timetable: TimeTable, lesson: Lesson, week_type: WeekType,
                    week_day_type: WeekDayType) -> None:
        match week_day_type:
            case WeekDayType.MONDAY:
                day = timetable.week_a.monday if week_type == WeekType.A else timetable.week_b.monday
            case WeekDayType.TUESDAY:
                day = timetable.week_a.tuesday if week_type == WeekType.A else timetable.week_b.tuesday
            case WeekDayType.WEDNESDAY:
                day = timetable.week_a.wednesday if week_type == WeekType.A else timetable.week_b.wednesday
            case WeekDayType.THURSDAY:
                day = timetable.week_a.thursday if week_type == WeekType.A else timetable.week_b.thursday
            case WeekDayType.FRIDAY:
                day = timetable.week_a.friday if week_type == WeekType.A else timetable.week_b.friday
            case _:
                raise RuntimeError("Unsupported week day")
        day.append(lesson)
