class House:
    def __init__(self, price):
        self.__price = price


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    
my_house = House(650000)
my_house.price = = 70000
print(my_house.price)