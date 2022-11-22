"""
Special methods/Magic methods/Dunder Method.
This special methods allow us to impelment operator overloading.

What is Operatot overloading?
1+2 = 3 but 'a'+'b' = ab 
The same + operator is actually doing sum on integeers while conctinating on strings. Its changing its behaviour based on object type.

This special methods always surround by __ 
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

emp1 = Employee('chinmay', 'nayak', 5000)
print(emp1) 

#Without __repr__ or __str__ the print will be: <__main__.Employee object at 0x7f9a57517e80>
#With __repr__ we can print as we wish : Employee(chinmay,nayak,5000)
#Its more for developer. print(emp1) = print(emp1.__repr__()) running in background
#With __str__ we can print as we wish : chinmay nayak : chinmay.nayak.comapny.com
#Its more for End users. print(emp1) = print(emp1.__str__()) running in background
