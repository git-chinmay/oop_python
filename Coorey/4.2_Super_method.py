"""
Adding __init__ to child class
Ex:- We want to add language to the Devloper class
"""

class Employee:

    raise_percent = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"{self.first} {self.last}"

    def raise_pay(self):
        return int(self.pay * self.raise_percent)




class Developer(Employee):
    raise_percent = 2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

emp1 = Developer('chinmay', 'nayak', 50000, 'python')
print(emp1.full_name())
print(emp1.prog_lang)

emp2 = Employee('Test', 'user', 50000)
print(emp2.pay)
print(emp2.raise_pay())