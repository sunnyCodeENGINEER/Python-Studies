import pyperclip, re

# phone number Regular Expression
phoneNumberRegex = re.compile(r"""
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # seperator
    (\d{3})                           # first three digits
    (\s|-|\.)                         # seperator
    (\d{4})                           # last for digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
""", re.VERBOSE)

# email Regular Expression
emailRegex = re.compile(r"""
    ([a-zA-Z0-9_.+%-]+)               # username
    (@)                               # @ symbol
    ([a-zA-Z0-9.-]+)                  # domain name
    (\.[a-zA-Z]{2,4})                 # dot something
""", re.VERBOSE)

# find matches in the clipboard
text = str(pyperclip.paste())
matches = []

phoneNumberHeading = """
\t\tThese are the phone Numbers found.
-------------------------------------------------

"""
matches.append(phoneNumberHeading)
for groups in phoneNumberRegex.findall(text):
    phoneNumber = "-".join([groups[0], groups[2], groups[4]])
    if groups[7] != "":
        phoneNumber += " x" + groups[7]
    matches.append(phoneNumber)

emailHeading = """
\t\tThese are the emails found.
-------------------------------------------------
"""
matches.append(emailHeading)

for groups in emailRegex.findall(text):
    email = "".join([groups[0], groups[1], groups[2], groups[3]])
    matches.append(email)

# copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy("\n" .join(matches))
    print("Copied to clipboard successfully")
    print("\n".join(matches))
else:
    print("There are no phone numbers or emails in the copied text.")
