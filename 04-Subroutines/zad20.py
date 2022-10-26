
def power(x,n):

    if n>1:
        return x*power(x,n-1)
    else:
        return x

x=2
n=21
print(power(x,n))