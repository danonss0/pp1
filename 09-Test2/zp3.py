def f(a2d):
    arr=[]
    for x in range(0,len(a2d[0])):
        sum=0
        for i in range(0,len(a2d)):
            sum+=a2d[i][x]
        arr.append(sum)

    return arr
print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )