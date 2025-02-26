class Xodim:
    def __init__(self, name, position, description):
        self.name = name
        self.position = position.capitalize()
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.position}) --- {self.description}"


print(" Boshqaruv Hodimlari:\n")
management_xodimi = [
    Xodim("Karzinka boshlig'i", "Boshqarish", "Ish jarayonini boshqaradi"),
    Xodim("Bug'altir", "Boshqarish", "Hisob-kitob ishlarini boshqaradi"),
]

for emp in management_xodimi:
    print(emp)

print("\n Savdo va xizmat ko‘rsatish xodimlari:\n")
sales_xodim = [
    Xodim("Sotuvchi", "Savdo", "Mijozlarga mahsulotlar bo‘yicha yordam beradi."),
    Xodim("Kassir", "Savdo", "Hisoblash ishini bajaradi."),
    Xodim("Omborchi", "Savdo", "Mahsulotlarni qabul qilish va saqlashni nazorat qiladi."),
    Xodim("Tozalash xodimi", "Savdo", "Gigiyena va tozalikni ta’minlaydi."),
]

for emp in sales_xodim:
    print(emp)

print("\n Yetkazib berish va yuklash xodimlari:\n")
supplier_xodim = [
    Xodim("Yuklovchi", "Yetkazish", "Tovarlarni joylashtirish"),
    Xodim("Haydovchi", "Yetkazish", "Yetkazib berish amaliyotini bajaradi"),
]

for emp in supplier_xodim:
    print(emp)


class Ombor:
    def __init__(self):
        self.__mahsulotlar = {}

    def mahsulot_qoshish(self, nomi, narxi, soni):
        if nomi in self.__mahsulotlar:
            self.__mahsulotlar[nomi]["soni"] += soni
        else:
            self.__mahsulotlar[nomi] = {"narxi": narxi, "soni": soni}

    def mahsulot_olish(self, nomi, soni):
        if nomi in self.__mahsulotlar:
            if self.__mahsulotlar[nomi]["soni"] > soni:
                self.__mahsulotlar[nomi]["soni"] -= soni
            else:
                del self.__mahsulotlar[nomi]

    def mahsulot_malumot(self, nomi):
        return self.__mahsulotlar.get(nomi, "Bunday mahsulot yo‘q!")

    def barcha_mahsulotlar(self):
        return self.__mahsulotlar


class Buyurtma:
    def __init__(self):
        self.__buyurtmalar = []

    def buyurtma_qoshish(self, mijoz, mahsulot, soni, ombor):
        mahsulot_info = ombor.mahsulot_malumot(mahsulot)
        if mahsulot_info != "Bunday mahsulot yo‘q!" and mahsulot_info["soni"] >= soni:
            ombor.mahsulot_olish(mahsulot, soni)
            self.__buyurtmalar.append({"mijoz": mijoz, "mahsulot": mahsulot, "soni": soni})
        else:
            print(f"{mahsulot} yetarli emas yoki mavjud emas!")

    def barcha_buyurtmalar(self):
        return self.__buyurtmalar


class Mijoz:
    def __init__(self, ism, telefon):
        self.__ism = ism  # Private o‘zgaruvchi
        self.__telefon = telefon  # Private o‘zgaruvchi

    def malumot_olish(self):
        return {"ism": self.__ism, "telefon": self.__telefon}
