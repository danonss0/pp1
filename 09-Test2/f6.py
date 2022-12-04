import csv
def f6(g,n1,n2):
    file=open('test.csv',newline='')
    t=[]
    sum=0
    for i in file:
       t.append(i)
    for i in range(len(t)):
        t[i]=(str(t[i])).split(",")
    for j in range(1,len(t)):
        if int(t[j][3])>=n1 and int(t[j][3])<=n2 and t[j][2]=="Female":
            sum+=1
    return sum

print(f6("Female",17,48))