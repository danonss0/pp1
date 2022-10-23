human=int(input("Enter the dog's age in human years: "))
if human<=2:
    dog=human*10.5
else:
    dog=((human-2)*4)+21
print(f"The dog's age in dog’s years is {dog}")
