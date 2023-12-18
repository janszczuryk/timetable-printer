import argparse
from app.service import TimeTableParserService, TimeTableRendererService


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='printer',
        description='Converts given html timetable to pdf form')

    parser.add_argument('html_file',
                        type=argparse.FileType('r', encoding='utf-8'),
                        help='path to html file with timetable')
    parser.add_argument('-o', '--output',
                        dest='output_filename',
                        required=False,
                        default='',
                        help='path to output pdf file')
    parser.add_argument('-i', '--id',
                        dest='table_id',
                        required=False,
                        default='table_78',
                        help='timetable\'s id inside html file')
    parser.add_argument('-t', '--template',
                        required=False,
                        default='portrait1',
                        help='template to be used to generate pdf file')
    parser.add_argument('-q', '--quiet',
                        required=False,
                        default=False,
                        action='store_true',
                        help='suppress all communicates')

    return parser.parse_args()


def determine_output_filename(table_id: str, arg_output_filename: str) -> str:
    return arg_output_filename or f"{table_id}.pdf"


def main() -> None:
    args = parse_arguments()

    timetable_parser = TimeTableParserService(args.html_file)
    timetable = timetable_parser.parse_timetable(args.table_id)

    output_filename = determine_output_filename(args.table_id, args.output_filename)

    if not args.quiet:
        timetable.print()

    timetable_renderer = TimeTableRendererService(timetable)
    timetable_renderer.render(args.template, output_filename)

    if not args.quiet:
        print(f"\nOutput pdf file saved as: {output_filename}")


if __name__ == "__main__":
    main()
