class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return f"{self.name} with price {str(self.price)} PLN"


class Phone(Product):
    def __init__(self, name, price, color):
        Product.__init__(self, name, price)
        self.color = color


    def __str__(self):
        return super().__str__() + f" and color {self.color}."




class TV(Product):
    def __init__(self, name, price, screen_size):
        super().__init__(name, price)
        self.screen_size = screen_size


    def __str__(self):
        return super().__str__() + f' and size of the screen {str(self.screen_size)}"'

# tv1 = TV("Samsung", 2000, 42)
# print(tv1)
# phone1 = Phone("Apple 14", 4800, "gray")
# print(phone1)