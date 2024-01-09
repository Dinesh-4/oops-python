class Car:
    #properties
    make = None
    model = None
    regno = None


    #setter

    def set_car(self, make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno

    #getter
    def get_name(self):
        return self.make


    # def __init__(self ,make, model, regno):
    #     self.make = make
    #     self.model = model
    #     self.rego = regno

    
    # def start(self):
    #     print("vruuuuu..... {} Engine is Online".format(self.make))




car1 = Car()
car1.set_car("BMW", "M4", "TN19 8888")
print(car1.get_name())

# car1.get_name()

car2 = Car()
car2.set_car("Audi", "A6", "TN19 4567")
print(car2.get_name())
