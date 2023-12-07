import re
from datetime import timedelta
from bs4 import BeautifulSoup
from model import TimeTable, Lesson


def parse(content: bytes) -> None:
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("table", {"id": "table_78"})

    timetable_id = table.attrs.get("id")
    teacher = table.find("thead").find("tr").find("th").text

    timetable = TimeTable(timetable_id, teacher)

    for row_index, row in enumerate(table.find("tbody").find_all("tr")):
        for column_index, column in enumerate(row.find_all("td")):
            if not column.has_attr("class"):
                continue

            class_ = column["class"].pop()

            if "notAvailable" in class_ or "empty" in class_:
                lesson = Lesson(0, 1, "", column.text.strip(), "", "")
            elif re.match("c_[0-9]+", class_):
                lesson = Lesson(
                    class_,
                    int(column["rowspan"]),
                    column.find("div", {"class": "line1"}).text.strip(),
                    column.find("div", {"class": "line2"}).find("span", {"class": "subject"}).text.strip(),
                    column.find("div", {"class": "line2"}).find("span", {"class": "activitytag"}).text.strip(),
                    column.find("div", {"class": "line3"}).text.strip() if column.find("div", {
                        "class": "line3"}) is not None else ""
                )
            else:
                continue

            add_lesson(timetable, lesson, column_index)
        print(f"[{calc_hour(row_index + 1)}] ---------------")

    # timetable.print()


def add_lesson(timetable: TimeTable, lesson: Lesson, column_index: int) -> None:
    print(lesson.lesson_name, column_index)
    if column_index % 2 == 0:
        if column_index == 0:
            timetable.week_a.monday.append(lesson)
        elif column_index == 2:
            timetable.week_a.tuesday.append(lesson)
        elif column_index == 4:
            timetable.week_a.wednesday.append(lesson)
        elif column_index == 6:
            timetable.week_a.thursday.append(lesson)
        elif column_index == 8:
            timetable.week_a.friday.append(lesson)
    else:
        if column_index == 1:
            timetable.week_b.monday.append(lesson)
        elif column_index == 3:
            timetable.week_b.tuesday.append(lesson)
        elif column_index == 5:
            timetable.week_b.wednesday.append(lesson)
        elif column_index == 7:
            timetable.week_b.thursday.append(lesson)
        elif column_index == 9:
            timetable.week_b.friday.append(lesson)


def calc_hour(index: int) -> str:
    # 07:00 <-> 19:15
    start_hour = timedelta(hours=7, minutes=0, seconds=0)
    hour = start_hour + timedelta(minutes=index * 15)
    return str(hour)


def main() -> None:
    # url = "http://pei.prz.rzeszow.pl/as/Zima2023_teachers_days_horizontal.html"
    # website = requests.get(url)

    with open("../Zima2023_teachers_days_horizontal.html", "rb") as file:
        content = file.read()

    parse(content)


if __name__ == "__main__":
    main()
