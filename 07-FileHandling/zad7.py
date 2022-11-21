file = open("countries.txt", "r")
i=1
for x in file:
    print(i,".",x)
    i+=1
    
file.close()