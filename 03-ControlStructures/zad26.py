code = '0805'
x=0
for x in range(0,3,1):
    pin =input("Enter the PIN code: ")
    if pin==code:
        print("PIN correct")
        break
    else:
        print("Incorrect...")
        x+=1
if x==3:
    print("Sorry, your payment card has been blocked.")
