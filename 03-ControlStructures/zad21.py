university= "UEK w Krakowie"
for x in range(1,len(university)*2,2):
    university = university[:x] + " " + university[x:]
print(university)