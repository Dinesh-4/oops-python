class Car:

    def __init__(self ,make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno


    def __str__(self):
        return("vruuuuu..... {} Engine is Online. Car No: {}".format(self.make, self.rego))


    # def start(self):
    #     print("vruuuuu..... {} Engine is Online. Car No: {}".format(self.make, self.rego))



#with __str__() funtion

car1 = Car("BMW", "M4", 4567 )
print(car1)
