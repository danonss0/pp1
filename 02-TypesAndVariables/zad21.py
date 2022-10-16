from random import randint


dice=randint(1,6)
#print("Number:",dice)
guess=int(input("Try to guess the number from the dice: "))
print(guess==dice)