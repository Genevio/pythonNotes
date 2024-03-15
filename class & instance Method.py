#class Method

"""
class student:
    name = "Akshara"
    age = 30

    def printall():
        print("name:" ,student.name)
        print("age :",student.age)

student.printall()
print(student.__dict__)

print(getattr(student, 'printall'))
getattr(student, "printall")()

student.__dict__['printall']()

"""

#instance methods

class Employee:
    name = "genevio"
    age = 25

    def printall(self,gender):
        print("Name: ",Employee.name)
        print("Age:",Employee.age)
        print("gender:", gender)

o=Employee()

o.printall("male")
#Employee.printall(o,"Male")

