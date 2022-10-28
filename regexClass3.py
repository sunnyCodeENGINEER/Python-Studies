import re

# GREEDY AND NONGREEDY MATCHING
# greedy matching
greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHa")
print(mo1.group())

# nongreedy matching
nonGreedyRegex = re.compile(r"(Ha){3,6}?")
mo2 = nonGreedyRegex.search("HaHaHaHaHa")
print(mo2.group())
