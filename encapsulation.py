class Computer:
    def __init__(self):
        self.__maxprice=100
    def sell(self):
        print(f"selling price:{self.__maxprice}")
    def setMaxPrice(self, price):
        self.__maxprice=price

c=Computer()
c.sell()

c.__maxprice=200
c.sell()
# use of setter function
c.setMaxPrice(200)
c.sell()