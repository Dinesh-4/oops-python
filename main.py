from store.Car import Car

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

