hours = input("Podaj liczbe godzin: ")

hours=float(hours)
wage = input("Podaj stawkę godzinową: ")

wage=float(wage)
if (hours>40):
   wage=wage*1.5
salary = hours*wage
print ('Wynagrodzenie: ',salary)
