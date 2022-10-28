import re

# MANAGING COMPLEX REGEXES
# re.VERBOSE
phoneRegex = re.compile(r"""
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # seperator
    \d{3}                         # first three digits
    (\s|-|\.)                     # seperator
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
""", re.VERBOSE)

# combining re.IGNORECASE, re.DOTALL, re.VERBOSE
someRegexValue = re.compile(r"foo", re.DOTALL | re.IGNORECASE | re.VERBOSE)
