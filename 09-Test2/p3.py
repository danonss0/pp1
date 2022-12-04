def f(array2D):
    
    arr=[]
    for x in range(0,len(array2D[0])):
        sum=0
        for i in range(0,len(array2D)):
            sum+=array2D[i][x]
        arr.append(sum)
    return arr

print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))