suma =0
licz=0
lista= []
while True:
    l=input("Wprowadź liczbę: ")
    if l=="gotowe":
        break
    try:

        lista.append(int(l))
        suma=suma+int(l)
        licz=licz+1
        
    except:
        print("Nieprawidlowe dane")
largest = None

for itervar in lista:
    if largest is None or itervar > largest :
        largest = itervar
smallest = None

for itervar in [9, 41, 12, 3, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar

print(suma,licz,largest,smallest)