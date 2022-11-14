arr=[-15,8,-31,47,-2,19]
maximum, minimum=0, 0
for i in range(0,len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
for i in range(0,len(arr)):
    if arr[i]<minimum:
        minimum=arr[i]
print(maximum," ",minimum)