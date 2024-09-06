from datetime import datetime

class Speed_ticket:
    def __init__(self, registration, time, speed_kph, speed_limit_kph) -> None:
        self._registration = registration
        self._time = time
        self._speed_kph = speed_kph
        self._speed_limit_kph = speed_limit_kph
    
    def get_registration(self):
        return self._registration
    
    def get_time(self):
        return self._time

    def __str__(self) -> str:
        return f"{self._registration}  time: {self._time},  speed: {self._speed_kph},  speed limit: {self._speed_limit_kph}"


if __name__ == "__main__":
    ticket1 = Speed_ticket("FY99401", datetime.fromisoformat("2022-01-03 07:22:33"), 72.289, 60)
    print(ticket1)