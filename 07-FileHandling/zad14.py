name=input("Wprowadź nazwę pliku")
file = open(name,encoding="Utf-8")
lines=0
for x in file:
    lines+=1
print(f"Fime name: {name}\nNumber of lines: {lines}")