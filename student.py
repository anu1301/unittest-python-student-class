from datetime import date, timedelta

class Student:
    """A student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # when an instance of the Student class is created the 
        # start_date value is set using the time the instance is created.
        self._start_date = date.today()
        # this does not take into account Leap Years
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property # denotes read only
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property # denotes read only
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

