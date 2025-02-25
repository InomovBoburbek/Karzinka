from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_info(self):
        pass

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class Food(Product):
    def get_info(self):
        return "Bu oziq-ovqat mahsuloti."

class Electronics(Product):
    def get_info(self):
        return "Bu elektron mahsulot."

class gigiyena(Product):
    def get_info(self):
        return "Bu kiyim mahsuloti."


food = Food()
electronics = Electronics()
clothing = gigiyena()


print(food.get_info())  
print(electronics.get_info()) 
print(clothing.get_info())  

