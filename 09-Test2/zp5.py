import re


def f(f_l,l_l):
    wynik=[]
    file=open('test.txt','r',encoding='UTF-8')
    wzorzec=re.compile(fr"\b{f_l}\S+{l_l}\b")
    for i in file:
        wynik+=wzorzec.findall(i)
    return len(wynik)

print(f("w","d"))