class InvalidAgeError(Exception):
    pass

class AgeChecker:
    def __init__(self, age):
        self.age = age

    def validate(self):
        if self.age < 18:
            raise InvalidAgeError("Age must be at least 18.")
        else:
            print("Age is valid.")

try:
    user_age = int(input("Enter your age: "))
    checker = AgeChecker(user_age)
    checker.validate()
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
