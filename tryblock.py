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

"""

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
print(len(dir(locals()['__builtins__'])))
