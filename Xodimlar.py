class Xodim:
    def __init__(self, name, position, description):
        self.name = name
        self.position = position
        self.description = description

    def __str__(self):
        return f"{self.name} – {self.description}"

print("Boshqaruv Hodimlari:\n")
management_employees = [
    Xodim("Do‘kon boshlig‘i", "Boshqaruv", "Ish jarayonini boshqaradi."),
    Xodim("Buxgalter", "Boshqaruv", "Hisob-kitob ishlari bilan shug‘ullanadi."),
]

for emp in management_employees:
    print(emp)

print("\n🛒 Savdo va xizmat ko‘rsatish xodimlari:\n")
sales_employees = [
    Xodim("Sotuvchi", "Savdo", "Mijozlarga mahsulotlar bo‘yicha yordam beradi."),
    Xodim("Kassir", "Savdo", "Kassa operatsiyalarini amalga oshiradi."),
    Xodim("Omborchi", "Savdo", "Mahsulotlarni qabul qilish va saqlashni nazorat qiladi."),
    Xodim("Tozalash xodimi", "Savdo", "Gigiyena va tozalikni ta’minlaydi."),
]

for emp in sales_employees:
    print(emp)

print("\nYetkazib berish va yuklash xodimlari:\n")
logistics_employees = [
    Xodim("Yuklovchi", "Yetkazib berish", "Tovarlarni joylashtiradi."),
    Xodim("Haydovchi", "Yetkazib berish", "Yetkazib berish xizmatini amalga oshiradi."),
]

for emp in logistics_employees:
    print(emp)
