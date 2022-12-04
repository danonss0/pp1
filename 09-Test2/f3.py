import re


def f3(t):
    c=[]
    warunek=re.compile(r"\b\d\d\b|\b\d\d\d\b")
    sum=0
    c+=warunek.findall(t)
    for i in c:
        sum+=int(i)
    return sum
print(f3("Przykładowe liczby parzyste to 16, 2, 114 oraz 1014, a także 8"))