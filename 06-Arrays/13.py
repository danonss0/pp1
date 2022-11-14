arr=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
sum=0
for i in range(0,len(arr)):
    for x in range(0,len(arr[0])):
        if arr[i][x]%2==0:
            sum+=arr[i][x]
print(sum)