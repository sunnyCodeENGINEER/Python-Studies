import os

# handling relative and absolute paths
a = os.path.abspath(".")
print(a)
b = os.path.abspath(r".\Scripts")
print(b)

c = os.path.relpath(r"C:\Windows", "C:\\")
print(c)


d = os.path.dirname(os.path.abspath("."))
print(d)
e = os.path.basename(os.path.abspath("."))
print(e)

f = os.path.split(os.path.abspath("."))
print(f)

g = os.path.abspath(".").split(os.path.sep)
print(g)

