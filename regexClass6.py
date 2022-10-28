import re

# case-insensitive matching
roboCopRegex = re.compile(r"robocop", re.IGNORECASE)
roboMo = roboCopRegex.findall("Robocop said hi to Mr. ROBOCOP right after beating captain rObOcOp")
print(roboMo)

# substituting strings with the sub() method
namesRegex = re.compile(r"Agent \w+")
namesMo = namesRegex.sub("Mr. Smith", "Agent Steve gave the secret documents to Agent Bob")
print(namesMo)

agentNamesRegex = re.compile(r"Agent (\w)\w*")
agentNamesMo = agentNamesRegex.sub(r"\1****", "Agent Steve gave the secret documents to Agent Bob")
print(agentNamesMo)
