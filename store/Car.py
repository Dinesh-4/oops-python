class Car:

    def __init__(self ,make, model, regno):
        self.make = make
        self.model = model
        self.rego = regno
        self.batt = 0

    def start(self):
        print("vruuuuu..... {} Engine is Online. Car No: {}".format(self.make, self.rego))

    def get_battery(self):
        print("Battery : {}%".format(self.batt))
        self.start()