# Day 10: OOP Example - Product Class

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is {self.price} rs")

    @classmethod
    def get_count(cls):
        print(f"Total number of products: {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        discounted_price = price - (price * discount / 100)
        print(f"Discounted price is {discounted_price}")


# Objects
p1 = Product("Phone", 10000)
p2 = Product("Laptop", 60000)
p3 = Product("Table", 5000)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()

p1.calc_discount(p1.price, 12)