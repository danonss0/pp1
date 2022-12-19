# class definition
class Student():
    
    # class variables
    id = 100000
    uni = "UEK Kraków"
    
    def __init__(self,name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        Student.id+=1
        self.id=str(Student.id)
    
    def __str__(self):
        return self.name +" " +self.surname + ", ("+ self.id+"), "+Student.uni
    
uczen1=Student("Anna","MAJ","Applied Informatics")
uczen2=Student("Łukasz","Doniec","Applied Informatics")

print(uczen1)
print(uczen2)