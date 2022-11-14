arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
maximum=0
longest=""
for i in range(0,len(arr)):
    if len(arr[i])>maximum:
        maximum=len(arr[i])
        longest=arr[i]
print("Names:",*arr," \nLongest name:",longest)