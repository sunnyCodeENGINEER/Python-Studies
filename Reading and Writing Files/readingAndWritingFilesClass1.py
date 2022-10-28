import os

a = os.path.join("usr", "bin", "spam")
print(a)

myFiles = ["accounts.txt", "details.txt", "invite.docx"]
for filename in myFiles:
    print(os.path.join("C:", "Users", "edonkor"))

# the current working directory
a = os.getcwd()
print(a)
os.chdir("C:\\Windows\\System32")
a = os.getcwd()
print(a)

# creating new folders
# os.makedirs(os.path.join("D:", "delicious", "walnut", "waffles"))

