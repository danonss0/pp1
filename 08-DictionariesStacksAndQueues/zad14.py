dic={
    'a':'alfa',
    'b':'bravo',
    'c':'charlie',

}
word=input("Wprowadz tekst: ")
spell=[]
for i in word:
    spell.append(dic[i])

print(" ".join(spell))