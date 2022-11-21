file = open('shopping.txt','a')
while True:
    print("Wprowadź 0 aby zakończyć")
    x=input("Wprowadź produkt: ")
    if x=="0":
        break
    else:
        file.write(x)
        file.write("\n")

file.close()