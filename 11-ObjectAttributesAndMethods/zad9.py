import random


class Arrays():

    @staticmethod
    def gen1(n,w):
        list=[]
        for i in range(n):
            list.append(w)
        print(list)
    def gen2(n,fr,to):
        list=[]
        for i in range(n):
            list.append(random.randint(fr, to))
        print(list)
    def gen3(array,fr,to):
        sum=0
        for i in array:
            if i >=fr and i<=to:
                sum+=1
            
        print(sum)    
num1=2
num2=8
val=5
Arrays.gen1(num1,val)
val_from=2
val_to=4
Arrays.gen2(num2,val_from,val_to)
array=[1,5,4,3,6,7,3,2]
Arrays.gen3(array,val_from,val_to)




