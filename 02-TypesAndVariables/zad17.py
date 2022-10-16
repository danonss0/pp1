from math import ceil


height=float(input("Type your height in cm: "))
inc=height/2.54
feet=inc//12
inch=ceil(inc-feet*12)
print(f"I am {height}, i.e. {feet} feet and {inch} inches")