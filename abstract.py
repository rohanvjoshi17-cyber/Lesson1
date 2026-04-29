from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Dog(Animal):
    def move(self):
        print("I can walk, jump, run and bark ")

class Lion(Animal):
    def move(self):
        print("I too can walk, jump, run and roar")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()