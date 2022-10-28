import os

# opening files with the open() function.
# reading single line documents.
helloFile = open(os.path.abspath("helloWorld.txt"), "r")
helloContent = helloFile.read()
print(helloContent)

# reading multiline documents.
sonnetFile = open(os.path.abspath("sonnet96.txt"))
sonnetContent = sonnetFile.readlines()
print(sonnetContent)

# writing to files with "w"
baconFile = open("bacon.txt", "w")
baconFile.write("Hello world!!!\n")
baconFile.close()

baconFile = open("bacon.txt", "a")
baconFile.write("Bacon is not a vegetable.")
baconFile.close()
baconFile = open("bacon.txt", "r")
baconContent = baconFile.read()
print(baconContent)
