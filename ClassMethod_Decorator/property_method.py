# Without @property


class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        return f"Instace value : {self.value}"
    

#Creating an instance of MYClass

obj = MyClass(42)

print(obj.display_value())


# With @property

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    @property
    def diameter(self):
        return 2 * self._radius
    @property
    def area(self):
        return 3.14 * self._radius**2
    

my_circle = Circle(5)

print(my_circle.radius)
print(my_circle.diameter)
print(my_circle.area)