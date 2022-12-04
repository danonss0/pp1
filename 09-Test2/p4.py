def f(dic,x,y):
    sum=0
    for k,v in dic.items():
        for i in v:
            if(i>=x and i<=y):
                sum+=i
    return sum

print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))