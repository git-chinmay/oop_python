"""
class variable
How to access it?
Looking inside the class and instances using __dict__
"""

class Employee:

    #class variable
    rasied_percent = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"Employee: {self.first} {self.last}."

    def payment(self):
        #return f"{self.full_name()} has received payment ${self.pay}."
        return f"{Employee.full_name(self)} has received payment ${self.pay}."

    def raise_amount(self):
        #return f"Raised amount is: {self.pay * Employee.rasied_percent}"
        return f"Raised amount is: {self.pay * self.rasied_percent}"


emp1 = Employee('chinmay', 'nayak', 50000)
print(emp1.full_name())
print(emp1.raise_amount()) #75000

print(emp1.__dict__)
print(Employee.__dict__)
emp1.rasied_percent = 2
print(emp1.__dict__)
print(Employee.__dict__)

print(emp1.raise_amount()) #10000 bcz we set the percent =2 it will noy work for other emp bcz we set it specific to emp1

emp2 = Employee('foo','bar', 50000)
print(emp2.raise_amount()) #75000