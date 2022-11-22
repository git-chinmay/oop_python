"""
When we add things print(1+2) in backend it uses __add__ method.
Here to add two emplyees salary we can use the same.
Another approach which is traditional is just create a addSalary() class method and call it Employee.addSalary()
Or we an just pass two emp instances as two inetegers 1+2 and in let the + operatot call our defined __add__ in backend.

Special methonds: https://docs.python.org/3/reference/datamodel.html#special-method-names
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def emailid(self):
        return f"{self.first}.{self.last}.comapny.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"

    def __str__(self):
        return f"{self.fullname()} : {self.emailid()}"

    def __add__(self, other):
        """self= emp1 & other=emp2"""
        return self.pay + other.pay

    @staticmethod
    def addSalary(pay1, pay2):
        return pay1+pay2

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('chinmay', 'nayak', 5000)
emp2 = Employee('john', 'nash', 6000)
print(emp1 + emp2) #Using special method
print(Employee.addSalary(emp1.pay, emp2.pay)) #Using traditional method
print(len(emp1)) #len(emp1)-->will call __len__(self)--> which runs len(chinmay nayak)-->which in background "chinmay nayak".__len__() = 13



