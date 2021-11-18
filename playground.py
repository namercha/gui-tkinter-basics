def add(*args):
    # print positional arguemnts
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 15, 32, 1))


def calculate(n, **kwargs):
    # type of kwargs is dict
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        self.make = kwargs.get("make")
        # self.color = kwargs["color"]
        self.color = kwargs.get("color")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

my_car_2 = Car(make="Nissan")
print(my_car_2.model)
