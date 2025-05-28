class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

times_three = Multiplier(3)

print(callable(times_three)) 
result = times_three(10)
print(result) 
