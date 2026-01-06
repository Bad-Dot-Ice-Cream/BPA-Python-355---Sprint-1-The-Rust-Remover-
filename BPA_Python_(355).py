print("\n")
print("Please input the following details for the laptop:")
name = input("User Name: ")
sku = input("SKU: ")
price = float(input("Price: "))
ram = input("RAM: ")
storage = input("Storage: ")
touchscreen = input("Touchscreen (Y/N): ")

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
        
def calculate_discount(percent):
            percent_process = price * 0.15
            percent = round(percent_process, 2)
            print("Discounted price > ",percent)

    
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
    calculate_discount(0.15)
spec_sheet()
