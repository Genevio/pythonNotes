#try block in python
#compile
#runtime
"""
try:
    a=5/0
except Exception as e:
    print(e)


try:
    a=10/0
except Exception as e:
    print(e)
else:
    print("value of A: ", a)



#try else finally

try:
    a=10/5
except Exception as e:
    print(e)
else:
    print("A's valueL" , a)
finally:
    print("Thanks")

#types of exceptions

print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))"""

#name error exception
try:
    print(a)
except NameError as e:
    print("A is not defined")

try:
    print(10/8)
except ZeroDivisionError as e:
    print("deno cant be zero")

try:
    a=int("gen")
except ValueError as e:
    print("please enter a num")

try:
    a=[2,5,7,8,9]
    print(a[10])
except IndexError as e:
    print("Invalid indx")
