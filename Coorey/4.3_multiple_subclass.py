"""
Lets have a Manager class
"""


class Employee:

    raise_percent = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"{self.first} {self.last}"

    def emailId(self):
        return f"{self.first}.{self.last}@company.com"

    def raise_pay(self):
        return int(self.pay * self.raise_percent)




class Developer(Employee):
    raise_percent = 2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.full_name()}")

    def add_emp(self, emp):
        if emp not in self.employees:
            print(f"{emp.emailId()} added")
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            print(f"{emp.emailId()} removed")
            self.employees.remove(emp)

emp1 = Developer('chinmay', 'nayak', 50000, 'python')
emp2 = Developer('Jack', 'Daniel', 40000, 'java')

mgr = Manager('Brad', 'Smith', 1000000, [emp1])
#mgr = Manager('Brad', 'Smith', 1000000)
mgr.print_emps()

mgr.add_emp(emp2)
mgr.print_emps()

mgr.remove_emp(emp1)
mgr.print_emps()

