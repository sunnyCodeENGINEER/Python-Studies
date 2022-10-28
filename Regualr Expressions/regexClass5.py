import re

# MAKING YOUR OWN CHARACTER CLASSES
vowelRegex = re.compile(r"[aieouAIEOU]")
mo1 = vowelRegex.findall("Robocop eats baby food. BABY FOOD.")
print(mo1)

# negative character class
consonantRegex = re.compile(r"[^aieouAIEOU]")
mo2 = consonantRegex.findall("Robocop eats baby food. BABY FOOD.")
print(mo2)

# THE CARET AND DOLLAR SIGN
# the caret ^, to check if the match is at the beginning of the sentence
beginWithHello = re.compile(r"^Hello")
mo3 = beginWithHello.search("Hello new world!!!")
print(mo3.group())

# the dollar $, to check if the sentence ends with the match
endswithNumber = re.compile(r"\d+$")
mo4 = endswithNumber.search("Your number is 42")
print(mo4.group())

# THE WILDCARD CHARACTER
# the dot, (.) character can match any character except a newline
atRegex = re.compile(r".at")
mo5 = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo5)

atRegex = re.compile(r".*?at")
mo5 = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo5)

# matching everything with the dot-star, .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print("\n")
print(mo.group(1))
print(mo.group(2))

# MATCHING NEWLINES WITH THE DOT CHARACTER
nonNewlineRegex = re.compile(".*")
nnlMo = nonNewlineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.")
print("\n")
print(nnlMo.group(0))

newLineRegex = re.compile(r".*", re.DOTALL)
nlMo = newLineRegex.search("\nServe the public trust.\nProtect the innocent.\nUphold the law.")
print(nlMo.group())
