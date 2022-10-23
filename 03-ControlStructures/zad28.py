n1=0
n2=1
print(n1,n2,end=" ")

for x in range(0,50,1):
    n=n1+n2
    print(n,end=" ")
    n1=n2
    n2=n
