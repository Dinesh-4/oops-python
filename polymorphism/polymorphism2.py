class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def move(self):
        print("Fly!")


car = Car("BMW", "M4")
boat = Boat("Titanic", "T2")
plane = Plane("Indigo", "Y6")

for x in (car, boat, plane):
    print(x.brand)
    print(x.model)
    x.move()






