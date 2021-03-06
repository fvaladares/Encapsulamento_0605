def decorator(f):
    def new_function():
        print("Extra Functionality")
        f()

    return new_function


@decorator
def initial_function():
    print("Initial Functionality")


# initial_function()
class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")


obj = House(200000)

print(obj.price)
obj.price = -150000
print(obj.price)
