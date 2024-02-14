from cart import *

phone = Phone( name=input("Phone brand: "), price=int(input("Phone price: ")), color=input("Phone color: ") )
tv1 = TV(input("TV brand: "), screen_size=int(input("TV screen size: ")), price=int(input("TV price: ")))
cart = Cart()
cart.add_product(phone)
cart.add_product(tv1)
cart.calculate_cart()
print(cart)
