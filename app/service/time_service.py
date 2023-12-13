from datetime import timedelta, datetime, timezone

ROW_DURATION_MINUTES = 15


class TimeService:

    @staticmethod
    def get_hour_by_row_index(row_index: int) -> str:
        start_hour = datetime(2000, 1, 1, 7, 0, 0, tzinfo=timezone.utc)
        hour = start_hour + timedelta(minutes=row_index * ROW_DURATION_MINUTES)
        return hour.strftime("%H:%M")

    @staticmethod
    def get_minutes_by_row_index(row_index: int) -> int:
        return ROW_DURATION_MINUTES * row_index
