class Car:

    def __init__(self ,make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno

    
    def start(self):
        print("vruuuuu..... {} Engine is Online".format(self.make))




car1 = Car("BMW", "M4", "TN19 8888")
car1.start()
