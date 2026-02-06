from datetime import datetime
from zoneinfo import ZoneInfo


class Time:
    """Represents a time of day."""

    def __init__(self):
        self.timestamp = datetime.now(ZoneInfo("America/Monterrey"))

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S %z")


lunch = Time()
print(lunch)