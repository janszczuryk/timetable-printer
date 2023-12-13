from .week_row import WeekRow


class Week:
    rows: list[WeekRow]

    def __init__(self):
        self.rows = []

    def print(self) -> None:
        print("[xx:xx]\tMonday\tTuesday\tWednesday\tThursday\tFriday")
        for row in self.rows:
            row.print()

    def get_last_row(self) -> WeekRow:
        return self.rows[-1]

    def add_row(self, row: WeekRow) -> None:
        self.rows.append(row)
