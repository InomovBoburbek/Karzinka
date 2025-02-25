class Employee:
    def __init__(self, name, position, description):
        self.name = name
        self.position = position
        self.description = description

    def __str__(self):
        return f"{self.name} – {self.description}"

print("Boshqaruv Hodimlari:\n")
management_employees = [
    Employee("Do‘kon boshlig‘i", "Boshqaruv", "Ish jarayonini boshqaradi."),
    Employee("Buxgalter", "Boshqaruv", "Hisob-kitob ishlari bilan shug‘ullanadi."),
]

for emp in management_employees:
    print(emp)

print("\n🛒 Savdo va xizmat ko‘rsatish xodimlari:\n")
sales_employees = [
    Employee("Sotuvchi", "Savdo", "Mijozlarga mahsulotlar bo‘yicha yordam beradi."),
    Employee("Kassir", "Savdo", "Kassa operatsiyalarini amalga oshiradi."),
    Employee("Omborchi", "Savdo", "Mahsulotlarni qabul qilish va saqlashni nazorat qiladi."),
    Employee("Tozalash xodimi", "Savdo", "Gigiyena va tozalikni ta’minlaydi."),
]

for emp in sales_employees:
    print(emp)

print("\nYetkazib berish va yuklash xodimlari:\n")
logistics_employees = [
    Employee("Yuklovchi", "Yetkazib berish", "Tovarlarni joylashtiradi."),
    Employee("Haydovchi", "Yetkazib berish", "Yetkazib berish xizmatini amalga oshiradi."),
]

for emp in logistics_employees:
    print(emp)
