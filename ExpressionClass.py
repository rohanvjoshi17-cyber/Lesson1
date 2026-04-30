class Expression:
    def calculate(self):
        return 0

class Add(Expression):
    def calculate(self):
        return self.a + self.b

class Subtract(Expression):
    def calculate(self):
        return self.a - self.b

class Multiply(Expression):
    def calculate(self):
        return self.a * self.b

class Divide(Expression):
    def calculate(self):
        return self.a / self.b


# ---- Main ----
print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

obj = None

if choice == 1:
    obj = Add()
elif choice == 2:
    obj = Subtract()
elif choice == 3:
    obj = Multiply()
elif choice == 4:
    obj = Divide()
else:
    print("Wrong choice")
    exit()

obj.a = float(input("Enter first number: "))
obj.b = float(input("Enter second number: "))

print("Result =", obj.calculate())
