from app.service import TimeTableParserService, TimeTableRendererService


def main() -> None:
    # TODO: support script arguments
    input_filename = "Zima2023_teachers_days_horizontal.html"
    table_id = "table_78"
    template = "timetable1"
    output_filename = "table_78.pdf"
    quiet = True

    with open(input_filename, "rb") as file:
        content = file.read()

    timetable_parser = TimeTableParserService(content)
    timetable = timetable_parser.parse_timetable(table_id)

    if not quiet:
        timetable.print()

    timetable_renderer = TimeTableRendererService(timetable)
    timetable_renderer.render(template, output_filename)


if __name__ == "__main__":
    main()
