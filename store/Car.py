class Car:

    #Class Attribute
    type = "Sedan"

    def __init__(self ,make, model, regno):
        self._make = make
        self.model = model
        self.rego = regno
        self.batt = 0
        if self.type == "Sedan":
            self.breakpow = "100%"
        elif self.type == "Hatchback":
            self.breakpow = "75%"

    def start(self):
        print("vruuuuu..... {} Engine is Online. Car No: {}".format(self._make, self.rego))

    def get_battery(self):
        print("Battery : {}%".format(self.batt))
        self.start()

    @classmethod
    def build_aston(cls, regno):
        g = cls("Aston Marton", "AB11", regno)
        g.start()
        return g
    
    @staticmethod
    def build_db11(regno):
        cls = Car
        g = cls("Audi", "A6", regno)
        g.start()
        return g
    
    @staticmethod
    def derive_max_speed():
        print("I am all independent car's @staticmethod")


    @property
    def make(self):
        return self._make
    
    #Property Attribute - this an extentions from above one 
    @make.getter
    def make(self):
        print("Returning {} {}".format(self.model, self.breakpow))
        return self._make
    
    @make.setter
    def make(self, make):
        print("Setting make to {}".format(make))
        self._make = make

    @make.deleter
    def make(self):
        print("Deleting {}...".format(self._make))
        del self._make
