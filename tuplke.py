#(,)
#()
#immutable & its is ordred

a= (1, 9.5 , True ,"genevio")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append("Virat")
print(b)
a=tuple(b)
print(a)

for i in a:
    print(i)

if "Virat" in a:
    print("name found")
else:
    print("Not Found")

print(len(a))

print("-------------")

"""a=(1,)
print(type(a))
del a"""

a=(1,2,7,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(7))

a=(1,2,7,4)
b=(5,6,7,8)
c=(a,b)
print(c)
print(c[0][2])

x=('gen',)*10
print(x)

a=(1,2,7,4)
b=(5,6,7,8)
print(min(a))
print(max(a))

