pln=int(input("Enter the amount in PLN: "))
x=pln//5
y=pln-x*5
z=y//2
c=y-z*2
print(f"The amount of PLN {pln} in coins: ")
print(f"5 zł - {x}\n2 zł - {z}\n1zł - {c}")
