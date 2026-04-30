num = int(input("Enter a number: "))

temp = num
sum = 0

n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** n)
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")