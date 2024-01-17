# Parent Class

class Automobile:
    def __init__(self, make, model, regno):
        #Instance Attributes
        self._make = make
        self.model = model
        self.rego = regno

    @property
    def make(self):
        return self._make
    
    #Property Attribute - this an extentions from above one 
    @make.getter
    def make(self):
        print("Returning {}".format(self.model))
        return self._make
    
    @make.setter
    def make(self, make):
        print("Setting make to {}".format(make))
        self._make = make

    @make.deleter
    def make(self):
        print("Deleting {}...".format(self._make))
        del self._make
    