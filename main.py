class Car:

    def __init__(self ,make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno

    
    def start(self):
        print("vruuuuu..... {} Engine is Online. Car No: {}".format(self.make, self.rego))




car1 = Car("BMW", "M4", "TN19 8888")
car1.rego = "TN19 1234"
car1.start()
del car1
car1.start()

