arr=[1,2,3,4,5,6,7,8,9]
i=0
even=[]
odd=[]
while i < len(arr):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
    i+=1
print("even:",*even,"odd:",*odd)
