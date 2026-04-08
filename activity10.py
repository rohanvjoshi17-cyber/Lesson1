num=int(input("Enter num to be check for prime number :"))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("It is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")