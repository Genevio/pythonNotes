class user:
    course = 'java'

o = user()

print(user.__dict__)
print(user.course) #class attr
print(o.__dict__)
print(o.course)
print(o.__dict__)
o.course = 'python'
print(o.__dict__)
print(o.course)


o2=user()
print(o2.course)