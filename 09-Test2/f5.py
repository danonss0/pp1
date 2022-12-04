import re


def f5(c):
    sum=[]
    file=open('test1.txt','r',encoding='UTF-8')
    warunek=re.compile(rf"{c}")
    for line in file:
        sum+=warunek.findall(line)
    return len(sum)
           

print(f5("v"))