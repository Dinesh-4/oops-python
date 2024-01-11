#without @classmethod.....


# class Car:

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def car_info(self):
#         return f"{self.brand} {self.model}"
    

# #creating an instance of the Car class
# my_car = Car("Toyota", "cooocoo")

# print(my_car.car_info())



#with @classmethod......


class Car:
    total_cars = 0
    singal_cars = 0
    multi_car = None

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
        if self.brand == "BMW":
            Car.singal_cars += 1  
            Car.multi_car = self.brand 


    @classmethod
    def display_total_cars(cls):
        return f"Total cars created: {cls.total_cars} &  {cls.singal_cars} {cls.multi_car} Cars Available!!!"



#creating an instance of the Car class
car1 = Car("Toyota", "Coro")
car2 = Car("BMW", "M4")
car3 = Car("BMW", "M4")



#Calling the class method
print(Car.display_total_cars())

