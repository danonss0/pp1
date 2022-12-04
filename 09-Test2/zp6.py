def f(age,course,average):
    import json
    file=open('test.json','r')
    jfile=json.load(file)
    total=0
    for i in jfile:
        if i["age"]>=age:
            for j in i['studies']['courses']:
                if j['name']==course:
                    sum=0
                    number=0
                    avr=0
                    for x in j['grades']:
                        sum+=x
                        number+=1
                        avr=sum/number
                    if avr>=average:
                        total+=1
                    
    return total       
                    
    

print(f(21, "statistics", 4))