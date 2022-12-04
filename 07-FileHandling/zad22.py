file= open("students.txt","r",encoding="UTF-8")
list=[]
for x in file:
    list.append(x)

for i in range(len(list)):
    list[i]=(str(list[i])).split(",")
print(list)
for j in range(1,6):
    if(int(list[j][2])<30):
        print(f"{list[j][0]} {list[j][1]} {list[j][4]}",end="")

file.close