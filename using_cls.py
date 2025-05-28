class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_counter()
