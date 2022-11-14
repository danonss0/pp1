arr=[[0,0,0],[0,0,0],[0,0,0]]
print(arr)

for x in range(0,len(arr[0])):
    arr[0][x]=1
    print(*arr[0])
    arr[0][x]=0