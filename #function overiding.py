#function overiding
#A(time) - B(time)
"""
class A:
   def time:
   pass
class b(A):
   def time:
   pass
"""

class Employee:
    def workinghrs(self):
        self.hrs=9
    def printhrs(self):
        print("Total working hrs :",self.hrs)

class Trainee(Employee):
    def workinghrs(self):
        self.hrs=6
    
    def updatedhrs(self):
        super().workinghrs()

"""employee = Employee()
employee.workinghrs()
employee.printhrs()"""

trainee = Trainee()
trainee.workinghrs()
trainee.printhrs()

trainee.updatedhrs()
trainee.printhrs()

