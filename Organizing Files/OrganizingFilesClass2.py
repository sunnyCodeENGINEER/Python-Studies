# safe deletes with the send2trash module
import send2trash

baconFile = open("bacon.text", "a") # creates the file
baconFile.write("Bacon is not a vegetable.")

baconFile.close()
send2trash.send2trash("bacon.txt")
