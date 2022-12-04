import re


def f(first_letter,last_letter):
    
    file = open('test.txt','r',encoding='UTF-8')
    wynik = []
    wzorzec= re.compile(fr"\b{first_letter}\w*{last_letter}\b")
    
    for x in file:
        wynik += wzorzec.findall(x)
    return len(wynik)

print(f("w","d"))