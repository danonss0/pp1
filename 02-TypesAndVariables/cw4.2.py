hours = input("Podaj liczbe godzin: ")
try:
    hours=float(hours)
    wage = input("Podaj stawkę godzinową: ")
    try:
        wage=float(wage)
        if (hours>40):
            wage=wage*1.5
        salary = hours*wage

        print ('Wynagrodzenie: ',salary)
    except:
         print("Błąd, podaj wartosć numeryczną")
except:
    print("Błąd, podaj wartosć numeryczną")
