print("\n")
print("Please input the following details for the laptop:")
name = input("User Name: ")
sku = input("SKU: ")
price = float(input("Price: "))
ram = input("RAM: ")
storage = input("Storage: ")
user_input_touch = input("Touchscreen (Y/N): ")
if user_input_touch.lower == "y":
    is_touchscreen = True
else:
     is_touchscreen = False

class Product:
    def __init__(self, name, sku, price):
        self.__name = name
        self.__sku = sku
        self.__price = price

        def get_name(self):
            return self.__name

        def get_sku(self):
            return self.__sku

        def get_price(self):
            return self.__price
        
def calculate_discount(discount=0.15):
    percent_process = price * discount  # (percent_process = 19.99 * 0.15)
    percent_rounded = round(percent_process, 2)  # $3.00
    finished_discount = price - percent_rounded  # (19.99 - 3.00)
    print("Discounted price > ",round(finished_discount, 2))

    
class Laptop(Product):
    def __init__(self, name, sku, price, ram, storage, touchscreen):
        super().__init__(name, sku, price)
        self.__ram = ram
        self.__storage = storage
        self.__touchscreen = touchscreen

def spec_sheet():
    print("\n")
    print(name)
    print("------")
    print(sku)
    print("$",price)
    calculate_discount()
spec_sheet()
