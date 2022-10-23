a = int(input("a: "))
b= int(input("b: "))
for x in range(1,b+1,1):
    print("*", end="")
print("\n", end="")  
for x in range(1,a-1,1):
    print("*",end="")
    for x in range(1,b-1,1):
        print(" ",end="")
    print("*")
    

for x in range(1,b+1,1):
    print("*", end="")