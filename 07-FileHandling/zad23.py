import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum=0
for i in range(3):
    sum+=int(temperatures[i])


print(sum/3)