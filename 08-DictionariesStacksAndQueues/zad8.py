from unicodedata import name


person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print("a)",person)
print("b)",person["name"])
print("c)",person["hobby"])
person["surname"]="Nowak"
print("d)",person)
person["married"]=False
print("e)",person)
person["gender"]="male"
print("f)",person)
person["hobby"].append("bicycle")
print("g)",person)
person["phone"]["work"]=313131444
print("h)",person)