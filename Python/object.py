
# class Persons:
#   def __init__ (self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#     print("My age is"+self.age)
#
#
#
# p1  = Persons("John","36")
# p1.myfunc()

# inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Arun","Sundar")
x.printname()