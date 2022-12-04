def f(dic,x,y):
    sum=0
    for i in dic:
        for k in dic[i]:
            if k>=x and k<=y:
                sum+=k
    return sum

print(f({"arr1":[2,6,5], "arr2":[7,1],"arr3":[2,9,8,1]}, 5, 10) )