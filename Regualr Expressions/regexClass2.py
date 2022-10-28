# MATCHING MULTIPLE GROUPS WITH THE PIPE
import re

heroRegex = re.compile(r"Batman|Tina Fey.")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

# piping on several patterns
batRegex = re.compile(r"Bat(man|mobile|copter|bat|cave)")
mo = batRegex.search("Batmobile lost a wheel.")
print(mo.group())
print(mo.group(1))

# OPTIONAL MATCHING WITH A QUESTION MARK
batRegex2 = re.compile(r"Bat(wo)?man")
mo3 = batRegex2.search("The Adventures of Batman.")
print(mo3.group())
mo4 = batRegex2.search("The Adventures of Batwoman.")
print(mo4.group())

# MATCHING ZERO OR MORE WITH THE STAR
# the group preceding the star needs not appear, instance can be zero
batRegex3 = re.compile(r"Bat(wo)*man")
mo5 = batRegex3.search("The adventures of Batman")
print("\n")
print(mo5.group())
mo6 = batRegex3.search("The Adventures of Batwoman")
print(mo6.group())
mo7 = batRegex3.search("The Adventures of Batwowowowowoman")
print(mo7.group())

# MATCHING ONE OR MORE WITH THE PLUS
# the group preceding the plus must appear at least once
batRegex4 = re.compile(r"Bat(wo)+man")
print("\n")
mo9 = batRegex4.search("The Adventures of Batwoman")
print(mo9.group())
mo10 = batRegex4.search("The Adventures of Batwowowowowoman")
print(mo10.group())

# MATCHING SPECIFIC REPETITIONS WITH CURLY BRACKETS
laughRegex = re.compile(r"(Ha){3}")
laughMo = laughRegex.search("HaHaHa")
print("\n")
print(laughMo.group())

laughRegex2 = re.compile(r"(Ha){3,5}")
laughMo2 = laughRegex2.search("HaHaHa")
print(laughMo2.group())

laughMo3 = laughRegex2.search("HaHaHaHaHa")
print(laughMo3.group())
