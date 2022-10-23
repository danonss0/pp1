for x in range(1,31,1):
    if x%3==0 and x%5!=0:
        print("THREE", end=" ")
    elif x%5==0 and x%3!=0:
        print("FIVE", end=" ")
    elif x%5==0 and x%3==0:
        print("BINGO", end=" ")
    else:
        print(x, end=" ")