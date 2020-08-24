# Python is an object oriented programming language.
# A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

# All classes have a function called __init__(), which is always executed when
# the class is being initiated. Use the __init__() function to assign values
# to object properties, or other operations that are necessary to do when the
# object is being created:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Objects can also contain methods. Methods in objects are functions that
# belong to the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# The 'self' parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class. It does not have
# to be named 'self' , you can call it whatever you like, but it has to be
# the first parameter of any function in the class:
class Person:
  def __init__(random_name, name, age):
    random_name.name = name
    random_name.age = age

  def myfunc(differentName):
    print("Hello my name is " + differentName.name)

p1 = Person("John", 36)
p1.myfunc()

# You can modify properties on objects like this:
p1.age = 40

# You can delete properties on objects by using the 'del' keyword:
del p1.age

# You can delete objects by using the del keyword:
del p1
