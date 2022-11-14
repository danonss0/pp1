arr=[[True,False],[True,True],[False,False]]
for i in range(0,len(arr)):
    for x in range(0,len(arr[0])):
        if arr[i][x]==True:
            arr[i][x]=False
        else:
            arr[i][x]=True

print(arr)