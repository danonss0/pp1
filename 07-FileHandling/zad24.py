import re

tekst="To be, or not to be, that is the question"
x=re.findall("[aeiou]",tekst)
print(len(x))