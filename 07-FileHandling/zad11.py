films = ['Minionki','Minionki 2','Fast X','8 mila','Baby Driver']
file = open('films.txt','w')
for i in range(0,len(films)):
    file.write(films[i])
    file.write("\n")
file.close()