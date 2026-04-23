class student:
    grade = 10
    name = "Rohan"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("My grade is", self.grade)

ob = student()
ob.introduction()
ob.details()