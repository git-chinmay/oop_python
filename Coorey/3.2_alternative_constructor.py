"""
Creating an alternative constructor using class method. This is different construnctor than __init__
This method widely used. One example is its used in datetime module

Here Example:
Lets say we are receiving a string format for each employee insted of first,last and pay format.
So each time we hve to process it before creating the instance. We can use alternative constructor for this processing.
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

# emp1 = Employee('chinmay', 'nayak', 50000)
# print(emp1.full_name())
# print(emp1.pay)

emp1_string = 'chinmay-nayak-50000'
emp1= Employee.from_empstring(emp1_string)
print(emp1.full_name())
print(emp1.pay)

"""
NOTE:- Once can say that why to bother crate a class method for thei processing. Instead we can just put those lines in to __init__
and each time we instantiate the class it would have automatically prcess the string. No need to separately call the class method for processing 
before calling the instance.

Answer is this is not making sense now as we are doing a basic splitting operation but in real time we may need to perform a big processing which inclused 
a lot of code and muluple such operations, so in that case we can not put all those processing inside __init__
It better to isolate them into classmethods and call them when needed.
"""