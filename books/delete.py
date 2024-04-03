import os

if os.path.exists("gene.txt"):
    os.remove("gene.txt")
else:
    print("not found")