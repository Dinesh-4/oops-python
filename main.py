class Car:

    def __init__(self ,make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno


    # def start(self):
    #     print("vruuuuu..... {} Engine is Online. Car No: {}".format(self.make, self.rego))



#without __str__() funtion

car1 = Car("BMW", "M4", "TN19 8888")
print(car1)

#output
#<__main__.Car object at 0x000001BB73BE9E50>