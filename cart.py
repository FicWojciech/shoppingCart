from products import *

class Cart:
    def __init__(self):
        self.__products_list = []
        self.__cart_value = 0


    def add_product(self, product):
        #if isinstance(product, Phone) or isinstance(product, TV):
        if isinstance(product, Product):
            if product not in self.__products_list:
                self.__products_list.append(product)
        else:
            print("We do not have product like this.")


    def calculate_cart(self):
        self.__cart_value = 0
        for element in self.__products_list:
            self.__cart_value += element.price


    def __str__(self):
        strData = '\nCart info, products list:'
        for product in self.__products_list:
            strData += "\n- " + str(product.name) + " " + str(product.price)
        strData += "\nTotal cart value: " + str(self.__cart_value)
        return strData




