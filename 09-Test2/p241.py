import re

textfile = open("test1.txt", 'r')
matches = []
reg = re.compile("\sa\w+")
for line in textfile:
    print(reg.findall(line))
   
textfile.close()