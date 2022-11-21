import random


file = open("randoms.txt","w",encoding="UTF-8")
for i in range(0,50):
    file.write(str(random.randint(50,999)))
    file.write("\n")
