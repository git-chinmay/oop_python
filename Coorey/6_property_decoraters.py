"""
Getters, Setters and Deleters
"""

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

# emp1 = Employee('chinmay', 'nayak')
# print(emp1.first) #chinmay
# print(emp1.email) #hinmay.nayak@email.com
# print(emp1.fullname()) #chinmay nayak

#What if we change the first name
# emp1.first = 'john'

# print(emp1.first) #john
# print(emp1.email) #hinmay.nayak@email.com
# print(emp1.fullname()) #john nayak

#We noticed that the email is still taking older firstname. This problem can be solved using a separate emailid() method
#but problem is that people who are using our class they need to refctaor theor code to use emailid() instaed of email attribute
#So what is the solution? Ans: Lets create a email() and convert it to attribute using property ecorator.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

# emp1 = Employee('chinmay', 'nayak')
# print(emp1.first) #chinmay
# print(emp1.email) #hinmay.nayak@email.com
# print(emp1.fullname()) #chinmay nayak

# #What if we change the first name
# emp1.first = 'john'

# print(emp1.first) #john
# print(emp1.email) #hinmay.nayak@email.com
# print(emp1.fullname()) #john nayak


############ Setters  ##################

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

# emp1 = Employee('chinmay', 'nayak')
# print(emp1.email)
# print(emp1.fullname)

# #Can we set the fullname
# emp1.fullname = "John Wick"
# print(emp1.fullname) #AttributeError: can't set attribute 'fullname'

#What is the solution. We can use another decoratot 'setter'

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, full_name):
        first, last = full_name.split(" ")
        self.first = first
        self.last = last


# emp1 = Employee('chinmay', 'nayak')
# print(emp1.fullname) #chinmay nayak
# print(emp1.email) #chinmay.nayak@email.com

# #Can we set the fullname
# emp1.fullname = "John Wick"
# print(emp1.fullname) #John Wick
# print(emp1.email) #John.Wick@email.com


##################### Deleter ##################
#We can also delete the attribute values using decorator deleter

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, full_name):
        first, last = full_name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name Deleted.")
        self.first = None
        self.last = None


emp1 = Employee('chinmay', 'nayak')
print(emp1.fullname) #chinmay nayak
print(emp1.email) #chinmay.nayak@email.com

del emp1.fullname

print(emp1.fullname) #None None
print(emp1.email) #None.None@email.com