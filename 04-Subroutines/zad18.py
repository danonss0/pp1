def calc(number):
    sum=0
    for x in range(0,len(number)):
        sum+=int(number[x])
    return sum

a="7182"
print(calc(a))