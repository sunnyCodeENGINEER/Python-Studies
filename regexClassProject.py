import pyperclip, re

# phone Regular Expression
phoneRegex = re.compile(r"""
    (\d{3}|\(\d{3}\))?               # area code
    (\s|-|\.)?                       # seperator
    (\d{3})                          # first 3 dagits
    (\s|-|\.)                        # seperator
    (\d{4})                          # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
""", re.VERBOSE)

# email Regular Expression
emailRegex = re.compile(r"""
    ([a-zA-Z0-9.-_%+]+)                # username
    (@)                                # @ symbol
    ([a-zA-Z0-9.-]+)                   # domain name
    (\.[a-zA-Z]{2,4})                # dot something
""", re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste())
# print(phoneRegex.findall(text))
# print(emailRegex.findall(text))
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[0], groups[2], groups[4]])
    if groups[7] != "":
        phoneNum += " x" + groups[7]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    email = "".join([groups[0], groups[1], groups[2], groups[3]])
    # matches.append(groups[0])
    matches.append(email)

print(matches)

# copy results to clipboard
if len(matches) >0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard successfully.")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")


