class Robot:
    def introduce(self):
        print("Hello! I am a robot.")
        print("My name is", self.name)
        print("My color is", self.color)
        print("I am", self.age, "years old")

r1 = Robot()

r1.name = input("Enter robot name: ")
r1.color = input("Enter robot color: ")
r1.age = input("Enter robot age: ")

print("\n--- Robot Introduction ---")
r1.introduce()