from tabulate import tabulate
from .week_row import WeekRow


class Week:
    rows: list[WeekRow]

    def __init__(self):
        self.rows = []

    def print(self) -> None:
        print(self)

    def __str__(self) -> str:
        headers = ['Hour', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        col = [5, 15, 15, 15, 15, 15]
        printable_rows = list(map(lambda row: [row.get_hour_start(), row.monday, row.tuesday, row.wednesday, row.thursday, row.friday], self.rows))
        return tabulate(printable_rows, headers=headers, maxcolwidths=col, tablefmt='simple_grid')

    def get_last_row(self) -> WeekRow:
        return self.rows[-1]

    def add_row(self, row: WeekRow) -> None:
        self.rows.append(row)
