class LogFunctionCall:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Function is being called")
        return self.func(*args, **kwargs)

@LogFunctionCall
def say_hello():
    print("Hello!")

say_hello()
