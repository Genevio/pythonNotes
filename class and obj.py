#class and object

"""
class - A class is a code template for creating objects. (blueprint /template for creating objects)
object - Objects are variables that contain data and functions that can be used to manipulate the data

#kia
model:seltos
color:black
brand:kia

#Hyundai
model:i20
color:white
brand:hyndai

#acccer braking ster


#class student:
#    name = "genevio"
#    age = "25"
class car():
    pass

a=10
print(type(a))
print(type(car))

seltos=car()
carens=car()
print(isinstance(seltos,car))
print(type(seltos))

"""
class Employee():
    name="Genevio"
    age=25
#these are class attributes
    
#attr method
#dot notation method

print(getattr(Employee,'name'))

print(getattr(Employee,'age'))

print(getattr(Employee,'gender','no such attr/no info reg this'))

#dot notation
print(Employee.name)
print(Employee.age)

#setattr
setattr(Employee,'name','Elizabeth')
print(Employee.name)

setattr(Employee,'gender','female')
print(Employee.gender)

#dotnotattion
Employee.city="Chennai"
print(Employee.city)

print(Employee.__dict__)
#delete attr
delattr(Employee,"city")
print(Employee.__dict__)
#using dot notation
del Employee.gender
print(Employee.__dict__)

#objects
# object_name = class_name(arg) #syntax

#E=Employee()

class user:
    course = 'python'

o=user()
print(user.__dict__) 
print(user.course) #printing class attr
print(o.__dict__)
print(o.course)
