import os

# get the size of a file
a = os.path.getsize(r"D:\Games\FIFA 22")
print(a)

# get a list of all files in a folder
b = os.listdir(r"D:\Games")
print(b)

# get the total size of a folder
totalSize = 0
for filename in b:
    totalSize += os.path.getsize(os.path.join(r"D:\Games", filename))
print(totalSize)

