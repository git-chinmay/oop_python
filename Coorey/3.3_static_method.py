"""
Static Method. A egular function we used inside a class because it has some logical conenction to our task.
It does not take any default self or cls arguments. Just an innocent function.
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"{self.first} {self.last}"

    @classmethod
    def from_empstring(cls, string):
        first, last, pay = string.split('-')
        #return Employee(first, last, pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'weekend'
        return 'workday'

import datetime
my_date = datetime.date(2023, 1, 16)
print(Employee.is_workday(my_date))
