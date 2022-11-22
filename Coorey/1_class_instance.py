"""
Class, Instance, Instance variable, Method, Method invokation types
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"Employee: {self.first} {self.last}."

    def payment(self):
        #return f"{self.full_name()} has received payment ${self.pay}."
        return f"{Employee.full_name(self)} has received payment ${self.pay}."


emp1 = Employee('chinmay', 'nayak', '50000')
print(emp1.full_name())
print(emp1.payment())