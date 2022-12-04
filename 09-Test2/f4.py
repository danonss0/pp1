def f4(d):
    sum=0
    for i in d:
        for k in d[i]:
            if k>=5 and k<=10:
                sum+=k
    return sum
print(f4({"arr1":[2,6,5], "arr2":[7,1],"arr3":[2,9,8,1]}))