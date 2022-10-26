def calc(text,letter):
    sum=0
    for x in range(0,len(text)):
        if text[x]==letter:
            sum+=1
    return sum

a="You never get a second chance to make a first impression"
b='e'
c="hello"
print(calc(a,b))