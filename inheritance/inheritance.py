# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lanme):
#         Person.__init__(self, fname, lanme)


# x = Student("Foo", "Boo")
# print(x.firstname)


# With Super() Function

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def greeting(self):
        print("Welcom", self.firstname, self.lastname, "year", self.graduationyear)


x = Student("Foo", "Boo", 1980)
print(x.firstname)
print(x.lastname)
print(x.graduationyear)
x.greeting()