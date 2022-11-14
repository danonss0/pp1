arr1 = [2,3,7,5,4]

print(*arr1)
print(len(arr1))
print(arr1[0])
print(arr1[1])
print(arr1[len(arr1)-1])
print(arr1[0]+arr1[4])
print(arr1[len(arr1)//2])
for i in range(0,len(arr1)):
    print(arr1[i]," ",end="")
print()
for i in range(0,len(arr1)//2+1):
    print(arr1[i]," ",end="")

