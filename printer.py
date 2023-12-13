import pickle

from app.service import TimeTableParserService, TimeTableRendererService


def main() -> None:
    # url = "http://pei.prz.rzeszow.pl/as/Zima2023_teachers_days_horizontal.html"
    # website = requests.get(url)

    input_filename = "Zima2023_teachers_days_horizontal.html"

    with open(input_filename, "rb") as file:
        content = file.read()

    table_id = "table_78"

    timetable_parser = TimeTableParserService(content)
    timetable = timetable_parser.parse_timetable(table_id)

    # with open("timetable.pyc", "wb") as timetable_file:
    #     pickle.dump(timetable, timetable_file)

    # with open("timetable.pyc", "rb") as timetable_file:
    #     timetable = pickle.load(timetable_file)

    timetable.print()

    # timetable_renderer = TimeTableRendererService(timetable)
    # timetable_renderer.render("timetable1")


if __name__ == "__main__":
    main()
