import re

# SEARCH() VS FINDALL()
# search()
phoneNumRegex = re.compile(r"(\d){3}-(\d){3}-(\d){4}")
mo1 = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo1.group())

# findall()
# findall() acts differently when groups are involved
phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo2 = phoneNumberRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo2)

phoneNumberRegex2 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
mo3 = phoneNumberRegex2.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo3)
