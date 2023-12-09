from datetime import timedelta

ROW_DURATION_MINUTES = 15


class TimeService:

    @staticmethod
    def get_hour_by_row_index(row_index: int) -> str:
        # 07:00 <-> 19:15
        start_hour = timedelta(hours=7, minutes=0, seconds=0)
        hour = start_hour + timedelta(minutes=row_index * ROW_DURATION_MINUTES)

        return str(hour)

    @staticmethod
    def get_minutes_by_row_index(row_index: int) -> int:
        return ROW_DURATION_MINUTES * row_index
