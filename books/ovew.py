try:
    file=open("gen.txt","a")
    file.write("this is sample by appdnd")
    file.close()

    file=open("gen.txt","r")
    for line in file:
        print(line)

except FileNotFoundError:
    print("Error:File not Found")
else:
    file.close()  