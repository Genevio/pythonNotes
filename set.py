"""#Sets - > (,)
#{ }
#sets are unordered
#Doesnot allow duplicates
#it cannot be changed

name={'Gen','Ben','DK'}
print(name)
print(type(name))
#accessing using Loop
for names in name:
    print(name)
#adding new element
name.add('sac')
print(name)

#updating 
a={'ak','vk','abd'}
name.update(a)

print(name)

name.remove('ak')
print(name)

name.discard('ak')
print(name)

name.clear()
print(name)

del name
print(name)

"""
a={1,2,3,4}
b={'a','b','c','d'}
c= a.union(b)
print(c)
a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}
"""
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)"""

a={5,6,7}
b={5,6,7}
c=a.isdisjoint(b)
print(c)

c=a.issubset(b)
print(c)