"""try:
    file=open("gene.txt","r")
    print(file.read( ))
except FileNotFoundError:
    print("Error:File not Found")
else:
    file.close()  """

file = open("msi.txt","r")
print(file.read()) 