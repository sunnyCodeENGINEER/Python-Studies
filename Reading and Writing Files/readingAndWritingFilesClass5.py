# Saving variables with the shelve module
import shelve
import pprint

# storing names of cats
shelfFile = shelve.open("mydata")
cats = ["Zophie", "Pooka", "Simaon"]
shelfFile["cats"] = cats
shelfFile.close()

# retrieving the names of the cats
shelfFile = shelve.open("mydata")
print(shelfFile["cats"])
shelfFile.close()

# saving files with pprint.pformat() function
cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
a = pprint.pformat(cats)
print(a)

fileObj = open("MyCats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")
fileObj.close()
