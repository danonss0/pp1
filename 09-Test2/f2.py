def f2(a1,a2):
    num1,num2=0,0
    
    for i in a1:
        if i>=10:
            num1+=1
    for i in a2:
        if i>=10:
            num2+=1
    if num1==num2:
        return True
    else:
        return False
print(f2([23,7,16,34],[1,18,79,20,6,111]))