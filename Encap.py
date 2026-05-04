class Computer:
    def __init__(self):
        self.maxprice = 900
    
    def sell(self):
        print("Selling Price: {}".format(self.maxprice))
    
    def setMaxprice(self, price):
        self.maxprice = price

c = Computer()
c.sell()

c.maxprice = 1000
c.sell()

c.setMaxprice(1000)
c.sell()