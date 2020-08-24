# Inheritance allows us to define a class that inherits all the methods and
# properties from another class.
# 'Parent class' is the class being inherited from, also called 'base class'.
# 'Child class' is the class that inherits from another class, also called
# 'derived class'.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname
# method:

x = Person("John", "Doe")
x.printname()

# Create a class named Student, which will inherit the properties and methods
# from the Person class:

class Student(Person):
    pass

# Use the Student class to create an object, and then execute the printname
# method:

x = Student("Mike", "Olsen")
x.printname()

# The __init__() function is called automatically every time the class is
# being used to create a new object.
# When you add the __init__() function, the child class will no longer inherit
# the parent's __init__() function.
class Student(Person):
    def __init__(self, fname, lname):
        pass
      #add properties etc.

# Python also have a super() function that will make the child class inherit
# all the methods and properties from it's parent:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# Add a year parameter, and pass the correct year when creating objects and add
# method called welcome:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
x = Student("Mike", "Olsen", 2019)
x.welcome()

# If you add a method in the child class with the same name as a function in the
# parent class, the inheritance of the parent method will be overridden.

