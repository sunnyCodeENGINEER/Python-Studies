import re

def myStripFunction(text:str, remove:str = ""):
    if remove != "":
        removeRegex = re.compile(r"{}".format(remove))
        removeMo = removeRegex.sub("", text)
        # return removeMo
        removeRegex = re.compile(r"\s{2,}")
        removeMo2 = removeRegex.sub(" ", removeMo)
        return removeMo2
    else:
        removeRegex = re.compile(r"(^\s*|\s*$)")
        removeMo = removeRegex.sub("", text)
        return removeMo



a = myStripFunction("Hello World.")
print(a)
b = myStripFunction("My name is Emmanuel, Emmanuel is my name. I was named Emmanuel at birth.", "Emmanuel")
print(b)

