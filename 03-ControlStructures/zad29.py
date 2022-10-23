n, x=-1, 0
sum=0
while n!=0:
    n=int(input("Enter number: "))
    sum=sum+n
    if n!=0:
        x+=1
print(f"RESULT: Quantity={x}, Sum={sum}, Mean={int(sum/x)}")