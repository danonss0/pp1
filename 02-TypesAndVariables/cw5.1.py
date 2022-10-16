suma =0
licz=0
while True:
    l=input("Wprowadź liczbę: ")
    if l=="gotowe":
        break
    try:

        suma=suma+int(l)
        licz=licz+1
    except:
        print("Nieprawidlowe dane")
print(suma,licz,suma/licz)