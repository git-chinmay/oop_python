"""
Inheritance Basic
"""

"""
Static Method. A egular function we used inside a class because it has some logical conenction to our task.
It does not take any default self or cls arguments. Just an innocent function.
"""

class Employee:

    raise_percent = 1.5

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

    def raise_pay(self):
        return int(self.pay * self.raise_percent)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'weekend'
        return 'workday'


class Developer(Employee):
    raise_percent = 2

emp1 = Developer('chinmay', 'nayak', 50000)
print(emp1.pay)
print(emp1.raise_pay())

emp2 = Employee('Test', 'user', 50000)
print(emp2.pay)
print(emp2.raise_pay())