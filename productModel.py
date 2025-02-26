from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_info(self):
        pass

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class Savat(Product):
    def __init__(self, savat_turi="kichik"):
        self.savat_turi = savat_turi  
        self.max_savat = 5 if savat_turi == "kichik" else 10
        self.savat = {}

    def add(self, mahsu_name, mahsu_price):
        if len(self.savat) < self.max_savat:
            if mahsu_name in self.savat:
                return f"{mahsu_name} savatda bor. Narx yangilanmaydi."
            self.savat[mahsu_name] = mahsu_price
            return f"{mahsu_name} savatga qo'shildi."
        else:
            return f"Savat to'lib ketdi! Maksimal {self.max_savat} ta mahsulot qo'shishingiz mumkin."

    def show(self):
        if not self.savat:
            return "Savat bo'sh."
        total = 0
        cart_items = "Savatdagi mahsulotlar:\n"
        for item_name, item_price in self.savat.items():
            cart_items += f"{item_name}: {item_price} so'm\n"
            total += item_price
        cart_items += f"\nJami narx: {total} so'm"
        return cart_items

    def get_info(self):
        return f"{self.savat_turi.capitalize()} savat"

class Food(Product):
    def get_info(self):
        return "Oziq-ovqat bo'lim"
    
    def __init__(self):
        self.food_list = [
            "Tuz","Un","Kofe","Yog'","Ko'k choy","Qora choy","Guruch","Nohot","Murch","Zira"
        ]
        self.food_narx = [
            5000,20000,3000,18000,12000,12000,16000,10000,1000,5000  
        ]
        
    def food_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.food_list)):
            print(f"{self.food_list[x]}: {self.food_narx[x]} so'm")
        
    def choose_food(self, chose):
        if 1 <= chose <= 10:
            select_food = self.food_list[chose - 1]
            select_narx = self.food_narx[chose - 1]
            return f"Siz {select_food} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

class Electronics(Product):
    def get_info(self):
        return "Elektron mahsulotlar bo'lim"
    def __init__(self):
        self.elec_list = [
            "Dazmol","Chanyutgich","Pichoq","Qoshiq va Vilka'","Choynak","Cook book","Termiz","Tova","Qozon","Mini torozi"
        ]
        self.elec_narx = [
            99900,699000,59900,64990,52500,15000,89900,149900,159900,59900  
        ]
        
    def elec_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.elec_list)):
            print(f"{self.elec_list[x]}: {self.elec_narx[x]} so'm")
        
    def choose_elec(self, chose):
        if 1 <= chose <= 10:
            select_elec = self.elec_list[chose - 1]
            select_narx = self.elec_narx[chose - 1]
            return f"Siz {select_elec} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

class Gigiyena(Product):
    def get_info(self):
        return "Shaxsiy gigiyena bo'lim"
    def __init__(self):
        self.ecolo_list = [
            "Shampun","Sovun","Goolgate","Zubnoy chotka'","Niqob","Aloe gel","Tala lux","Billur","Gupka","Latta Delfin"
        ]
        self.ecolo_narx = [
            39900,199000,15900,14990,22500,15000,19900,19900,1900,5900  
        ]
        
    def ecolo_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.ecolo_list)):
            print(f"{self.ecolo_list[x]}: {self.ecolo_narx[x]} so'm")
        
    def choose_ecolo(self, chose):
        if 1 <= chose <= 10:
            select_ecolo = self.ecolo_list[chose - 1]
            select_narx = self.ecolo_narx[chose - 1]
            return f"Siz {select_ecolo} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

    
class Meal(Product):
    def get_info(self):
        return "Go'sht maxsulotlar bo'lim"
    def __init__(self):
        self.mel_list = [
            "Mol go'shti","Qo'y go'shti","Tovuq go'shti","Tovuq qanot'","Baliq","Qiyma yog'siz","Jigar","Qiyma yog'li","kalbasa","Sasiska"
        ]
        self.mel_narx = [
            119900,109900,99900,14990,55500,119900,89900,39900,45900,29900  
        ]
        
    def mel_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.mel_list)):
            print(f"{self.mel_list[x]}: {self.mel_narx[x]} so'm")
        
    def choose_mel(self, chose):
        if 1 <= chose <= 10:
            select_mel = self.mel_list[chose - 1]
            select_narx = self.mel_narx[chose - 1]
            return f"Siz {select_mel} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

    
class Water(Product):
    def get_info(self):
        return "Ichimlik bo'lim"
    def __init__(self):
        self.wat_list = [
            "Coco Cola: 1l","Pepsi: 1l","Fanta: 1l","Sprite: 1l","Coco Cola: 0,5l","Pepsi: 0,5l","Fanta: 0,5l","Sprite: 0,5l","Suv: 1l","Suv: 0,5l"
        ]
        self.wat_narx = [
            12900,12900,11900,11900,6900,6900,5900,5900,4900,1900  
        ]
        
    def wat_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.wat_list)):
            print(f"{self.wat_list[x]}: {self.wat_narx[x]} so'm")
        
    def choose_wat(self, chose):
        if 1 <= chose <= 10:
            select_wat = self.wat_list[chose - 1]
            select_narx = self.wat_narx[chose - 1]
            return f"Siz {select_wat} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

    
    
class VegFru(Product):
    def get_info(self):
        return "Sabzavot va meva bo'lim"
    def __init__(self):
        self.vegfru_list = [
            "Sabzi: 1kg","Kartoshka: 1kg","Piyoz: 1kg","Qizil lovlagi: 1kg","Pamidor: 1kg","Bodiring: 1kg","Olma: 1kg","Nok: 1kg","Banan: 1kg","Kiwi: 1kg"
        ]
        self.vegfru_narx = [
            6900,6900,4900,5900,6900,6900,5900,5900,4900,11900  
        ]
        
    def vegfru_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.vegfru_list)):
            print(f"{self.vegfru_list[x]}: {self.vegfru_narx[x]} so'm")
        
    def choose_vegfru(self, chose):
        if 1 <= chose <= 10:
            select_vegfru = self.vegfru_list[chose - 1]
            select_narx = self.vegfru_narx[chose - 1]
            return f"Siz {select_vegfru} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"

    
class Candiy(Product):
    def get_info(self):
        return "Shirinlik bo'lim"
    def __init__(self):
        self.cand_list = [
            "Shkalad: 1kg","Snikers: 1kg","Bountiy: 1kg","KitKat: 1kg","Pirannik: 1kg","Chopli maroshni","Nonli maroshni","Maroshni: 1kg","Kinder: 1kg","Kiwili tort"
        ]
        self.cand_narx = [
            6900,6900,4900,5900,6900,6900,5900,5900,4900,111900  
        ]
        
    def cand_option(self):
        print("Tanlashingiz mumkin:")
        for x in range(len(self.cand_list)):
            print(f"{self.cand_list[x]}: {self.cand_narx[x]} so'm")
        
    def choose_cand(self, chose):
        if 1 <= chose <= 10:
            select_cand = self.cand_list[chose - 1]
            select_narx = self.cand_narx[chose - 1]
            return f"Siz {select_cand} nomli maxsulotni savatga soldingiz. Narxi: {select_narx} so'm"
        else:
            return "Iltimos maxsulotlarni tanlash uchun 1 dan 10 gacha bo'lgan raqamlardan foydalaning!"


