num=int(input("Enter number to be checked: "))
if num>50:
    print("The number is greater than 50")
    if num%2==0:
        print("And it is Even")
    else:
        print("And it is Odd")
else:
    print("it is not greater than 50")