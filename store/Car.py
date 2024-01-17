from .Automobile import Automobile

# Child Class

class Car(Automobile):

    #Class Attribute
    type = "Sedan"

    def __init__(self ,make, model, regno):
        super().__init__(make, model, regno)
        self.batt = 0
        if self.type == "Sedan":
            self.breakpow = "100%"
        elif self.type == "Hatchback":
            self.breakpow = "75%"

    # Build from Parent
    @classmethod
    def build_from_automobile(cls, d: Automobile):
        c = cls(d.make, d.model, d.rego)
        return c
    
    def start(self):
        print("vruuuuu..... {} Engine is Online. Car No: {}".format(self._make, self.rego))

    def get_battery(self):
        print("Battery : {}%".format(self.batt))
        self.start()

    # Build from Child
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

