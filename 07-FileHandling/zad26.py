import re

text="crane, teeth, speaks, dream, creepy, tracksuit"
x=re.findall("\w{6}",text)
for i in range(0,len(x)):
    print(f"{x[i]},")
    
