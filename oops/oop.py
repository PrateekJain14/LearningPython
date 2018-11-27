# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))
# PYTHON INBUILT FUNCTION TO ADD
class Kettle(object):

    # Class attribute is one that is hared by all the instances of a class for eg
    power_source = "Electricity"

    # In python init method in class is a default constructor as shown below
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


# Making object of class Kettle and passing 2 parameters
Kenwood = Kettle("Kenwood", 8.25)
print(Kenwood.make)
print(Kenwood.price)

Kenwood.price = 9.25
print(Kenwood.price)

hamilton = Kettle("Hamilton", 12.2)

print("Models: {} = {}, {} = {}".format(Kenwood.make, Kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(Kenwood)
print(Kenwood.on)

print("*" * 80)

# making an attribute outside the class for Kenwood instance (INSTANCE VARIABLE)
Kenwood.power = 1.5
print(Kenwood.power)
Kettle.power_source = "atomic"
Kenwood.power_source = "gas"
print("*" * 80)
print(Kettle.power_source)
print(Kenwood.power_source)
print(hamilton.power_source)


print(Kettle.__dict__)
print(Kenwood.__dict__)
print(hamilton.__dict__)