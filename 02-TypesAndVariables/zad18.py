a=float(input("Podaj bok a:"))
b=float(input("Podaj bok b: "))
c=float(input("Podaj bok c: "))
p=(a+b+c)/2
pole=(p*(p-a)*(p-b)*(p-c))**(1/2)
print(f"Pole trójkąta: {pole}")