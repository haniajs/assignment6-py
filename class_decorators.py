class add_greeting:
    def __init__(self, cls):
        self.cls = cls
    
    def __call__(self, *args, **kwargs):
        instance = self.cls(*args, **kwargs)
        
        def greet():
            return "Hello from Decorator!"
        instance.greet = greet
        return instance

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Afnan")
print(p.greet())  
