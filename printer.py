import re
from bs4 import BeautifulSoup
from app.model import TimeTable, Lesson, WeekType, WeekDayType
from app.service import TimeService


def parse(content: bytes, print_at_loading=False) -> None:
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("table", {"id": "table_78"})

    timetable_id = table.attrs.get("id")
    teacher = table.find("thead").find("tr").find("th").text

    timetable = TimeTable(timetable_id, teacher)

    for row_index, row in enumerate(table.find("tbody").find_all("tr")):
        print(f"[{TimeService.get_hour_by_row_index(row_index)}] ---------------") if print_at_loading else None

        for column_index, column in enumerate(row.find_all("td")):
            if not column.has_attr("class"):
                continue

            class_ = column["class"].pop()

            if "notAvailable" in class_ or "empty" in class_:
                lesson = Lesson("", row_index, 1, "", column.text.strip(), "", "")
            elif re.match("c_[0-9]+", class_):
                lesson = Lesson(
                    class_,
                    row_index,
                    int(column["rowspan"]),
                    column.find("div", {"class": "line1"}).text.strip(),
                    column.find("div", {"class": "line2"}).find("span", {"class": "subject"}).text.strip(),
                    column.find("div", {"class": "line2"}).find("span", {"class": "activitytag"}).text.strip(),
                    column.find("div", {"class": "line3"}).text.strip() if column.find("div", {
                        "class": "line3"}) is not None else ""
                )
            else:
                continue

            print(f"{column_index} - Dur: {lesson.duration_index}  {lesson.lesson_name}") if print_at_loading else None

            (week_type, week_day_type) = determine_weekday(timetable, row_index)

            add_lesson(timetable, lesson, week_type, week_day_type)

    timetable.print()


def determine_weekday(timetable: TimeTable, row_index: int) -> (WeekType, WeekDayType):
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


def add_lesson(timetable: TimeTable, lesson: Lesson, week_type: WeekType, week_day_type: WeekDayType) -> None:
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


def main() -> None:
    # url = "http://pei.prz.rzeszow.pl/as/Zima2023_teachers_days_horizontal.html"
    # website = requests.get(url)

    with open("Zima2023_teachers_days_horizontal.html", "rb") as file:
        content = file.read()

    parse(content)


if __name__ == "__main__":
    main()
