#init method in python
"""
class user:
    def __init__(self,name):
        print("call when new instances created")
        self.name = name
    
    def printall(self):
        print(self.name)

o=user("Genevio")
o.printall()
o1=user("AK")
o1.printall()
o2=user("Gen")

"""

#property decorator
"""
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.msg = self.name +" is " + str(self.age) + "  years old"
    
    @property
    def msg(self):
        return self.name +" is " + str(self.age) + "  years old"

o=user("Gen",25)
print(o.name)
print(o.age)
print(o.msg)
o.age=45
print(o.msg)
o.name="vk"
print(o.name)
"""

#property Decorator getter and setter

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,t):
        if t < 0 or t > 500:
            print("invalid number given")
        else:
            self._total=t
        
    
o=student(440)
print("total: ", o.total)
print("avg: ",o.average)
o.total=590
print("total: ", o.total)
print("avg: ",o.average())
