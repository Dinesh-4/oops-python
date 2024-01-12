# Without @staticmethod


class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        return f"Instace value : {self.value}"
    

#Creating an instance of MYClass

obj = MyClass(42)

print(obj.display_value())


#with @staticmethod

class MathOperations:

    @staticmethod
    def add(x, y):
        return x + y


print(MathOperations.add(1, 2))