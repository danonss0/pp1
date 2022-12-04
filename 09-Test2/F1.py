def f1(a):
    b=[]
    for i in range(len(a)):
        if a[i]%2==0:
            b.append(a[i])
    return b
print(f1([13,7,4,16,3,12,8]))