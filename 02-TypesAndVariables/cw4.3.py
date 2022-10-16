inp=input("Podaj wartość: ")
try:
    inp=float(inp)
    if inp > 0.0 and  inp<= 1.0:
        if inp > 0.0 and  inp< 0.5:
            print("2,0")
        if inp >=0.5 and inp <0.6:
            print("3,0")
        if inp >=0.6 and inp <0.7:
            print("3,5")
        if inp >=0.7 and inp <0.8:
            print("4,0")
        if inp >=0.8 and inp <0.9:
            print("4,5")
        if inp >=0.9 and inp <=1.0:
            print("5,0")
    else:
        print("Błąd, podaj wartosć numeryczną")
except:
    print("Błąd, podaj wartosć numeryczną")



