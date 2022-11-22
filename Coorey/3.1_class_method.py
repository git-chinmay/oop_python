"""
class methods
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
    
    @classmethod
    def set_percent(cls, percent):
        cls.rasied_percent = percent



emp1 = Employee('chinmay', 'nayak', 50000)
emp2 = Employee('Jack', 'Daniel', 40000)

print(Employee.rasied_percent)
print(emp1.rasied_percent)
print(emp2.rasied_percent)

#Employee.set_percent(2)
#We can set it by instance also but it soes not make any sense and people usually dont do it
emp1.set_percent(3)

print(Employee.rasied_percent)
print(emp1.rasied_percent)
print(emp2.rasied_percent)