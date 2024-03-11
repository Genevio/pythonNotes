#Functions- dividing a larger program into blocks are called functions
##types - user defined & standard lib fun
#syntax
"""
def fun_name(para_list):
    //function
"""



#No return type without arg function
"""
def add():
    a=int(input("enter the val of A: "))
    b=int(input("enter the val of B: "))
    c=a+b
    print("Total", c)
add()

#No return type with Arg fun
def sub(a,b):
    c=a-b
    print("ans" , c)

sub(25,2)


#Return type without Arg function
def mul():
    a=int(input("enter the val of A: "))
    b=int(input("enter the val of B: "))
    c=a*b
    return c

x=mul()
print(x)


#return type with arg func
def div(a,b):
    c=a/b
    return c
x=div(50,2)
print("div", x)

#arbitrary arg func

def grade_10(*students):
    print(students)
    for user in students:
        print(user)
grade_10("Gen","ben","Dk")



def gradeA(*student):
    for user in student:
        print(user)
        gradeA("gen")



#keyword arguments in python

def msg(name,age):
    print(name ,"age is", age)
msg(age=25,name="gen")

#Arbitary keyword arg
def biodata(**data):
    print(data)
biodata(name="genevio",age=25,gender="male")

#default parameter function

def user(name,city="chennai"):
    print(name,"he/she is from", city)
user("Genevio","Trivandrum")
user("Dk")

#passing list as an arg fun
def total(marks):
    return sum(marks)
print("Total:",total([55,78,688,78,90]))
"""

#recursive function
#5!=1*2*3*4*5=120

def factorial(x):
    if x==1:
        return 1
    else:
        return(x * factorial(x-1))
    
print("factorial:", factorial(8))


#5*fact(4)
#5*4*fact(3)
#5*4*3*fact(2)
#5*4*3*2*1

"""


