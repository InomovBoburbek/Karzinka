class SecuritySystem:
    def __init__(self , name , state = False):
        self.name = name
        self.__state = state
    def change_state(self , code , newstate):
        if code != "code11":
            return "XAtolik"
        if newstate == "1":
            self.__state = True
        elif newstate == "0":
            self.__state = False
        else:
            return "Error"
    def get_state(self , code):
        if code != "code11":
            return "Error"
        if self.__state == False:
            return "off"
        return "on"
class Camera(SecuritySystem):
    def __init__(self , name, resolution : int , state=False , nvision = False , record=False):
        super().__init__(name , state)
        self.__resolution = resolution
        self.__nvision = nvision
        self.__record = record
    def change_nvision(self , code , vision):
        if code != "code11":
            return "XAtolik"
        if vision == "1":
            self.__nvision = True
        elif vision == "0":
            self.__nvision = False
        else:
            return "Error"
    def get_nvision(self , code):
        if code != "code11":
            return "Error"
        if self.__nvision == True:
            return "on night vision"
        return "off night vision"
    def get_resolution(self , code):
        if code != "code11":
            return "Error"
        if self.__resolution >= 1080:
            return (f"Resolution : {self.__resolution}\nkamera yaxshi sifat bilan videoga oladi")
        return (f"Resolution : {self.__resolution}"
                f"Kamera yuqori sifatda olmaydi")
    def change_record(self , code , state):
        if code != "code11":
            return "Xatolik Mavjud"
        if state == "1":
            self.__record = True
            return f"{self.name} video olish boshlandi"
        elif state == "0":
            self.__record = False
            return f"{self.name} video olish tugatildi"
        else:
            return "Error Admin"
    def getrecordstate(self , code):
        if code != "code11":
            return "Error Code"
        if self.__record == True:
            return f"{self.name} kamera video olmoqda"
        elif self.__record == False:
            return f"{self.name} kamera video olmayabdi"
        return "Error Admin"
class TempratureSystem(SecuritySystem):
    def __init__(self , name  , gradus , maxx : int , minn : int ,  state = False):
        super().__init__(name , state)
        self.__gradus = gradus
        self.maxx = maxx
        self.minn = minn

    def change_gradus(self , code , graduss):
        if code != "code11":
            return "Error Admin"
        if self.minn <= graduss <= self.maxx:
            self.__gradus = graduss
            return f"Harorat {graduss} ga o'zgartirildi"
        return f"Harorat {self.minn} va {self.maxx} oralig'ida bo'lishi lozim , hozirgi harorat{self.__gradus} ! ! !"

    def get_gradus(self , code):
        if code != "code11":
            return "Error Admin"
        return f"Harorat {self.__gradus} *C"

class Parking:
    def __init__(self , capacity : int):
        self.capacity = capacity
        self.cars_number = set()
    def add_cars(self , num):
        if len(self.cars_number) < self.capacity:
            self.cars_number.add(num)
            return f"{num} raqamli mashina parkovkamizga qo'yildi , etr"
        return "Parkovka to'lgan , uzur mashinangizni boshqa joyga qo'ya qoling"
    def remove_cars(self , num):
        """CAR ochirishi"""
        if num in self.cars_number:
            self.cars_number.remove(num)
            return f"{num} parkovkada chiqarib yuborildi"
        return f"{num} buynday avtomobil parkovkada mavjud emas , adashdingiz"
