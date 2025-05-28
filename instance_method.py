class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!.. And his breed is {self.breed}.")

dog1 = Dog("Tommy", "Akita")
dog1.bark()
