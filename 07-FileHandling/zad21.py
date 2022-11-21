file = open("tabela.txt","w",encoding="UTF-8")
for i in range(3,15):
    file.write(str(i)+","+str(i*i)+","+str(i*i*i))
    file.write("\n")
file.close()