### With Decorator ###

def my_decorator(func):
    def wrapper():
        print("Something is happening before the {} funtion is called.".format(func.__name__))
        func() #call the original function 
        print("Something is happening after the {} funtion is called.".format(func.__name__))
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


### Without Decorator ###
print(end="\n")

def log_before_and_after(func):
    print(f"Before {func.__name__} is Called.")
    func()
    print(f"Before {func.__name__} is Called.")


def greeting():
    print("Hello, World!")


log_before_and_after(greeting())


