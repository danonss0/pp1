file = open('numbers.txt','r')
suma=0
for x in file:
    suma+=int(x)
print(suma)
file.close()