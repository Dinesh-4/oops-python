from store.Car import Car
from store.Automobile import Automobile
from store.Bike import Bike

car1 = Car("BMW", "M4", 4567 )
car1.start()

car1.batt = 50

# Call with Object Instance
car1.get_battery()

# Call with Class

Car.get_battery(car1)
print(Car.type)

a = Car.build_aston("TN33HH1234") #Classmethod
b = Car.build_db11("TN33RE2345") #Staticmethod

Car.derive_max_speed()

#calling property - getter
print(a.make)


#property setter
a.make = "Marton"
a.make = "Volvo"
print(a.make)

car1.make = "WMB"
print(car1.make)

#class attribute
Car.type = "heyden"
print(Car.type)

# Property delete
# del a.make
# print(a.make)


#-----------------
a.type = "Hatchback"
print("A's Type : " + a.type)
print(a.make)


#------------------------------
#Automobile class

d = Automobile("Bugadii", "N3", "TN89R1234")
# d.make = "Bugadii 8D"
print(d.make)

c = Car.build_from_automobile(d)
c.start()


#------------ BIke

B = Bike("KTM", "Duke", "TN23N1243")

B.make = "KTM TM"
print(B.make)



