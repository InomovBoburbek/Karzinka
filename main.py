from productModel import Food,Electronics,Gigiyena,Meal,Water,VegFru,Candiy,Savat

food = Food()
electronics = Electronics()
eco = Gigiyena()
meal = Meal()
water = Water()
vegfru = VegFru()
candiy = Candiy()
savat1 = Savat()
savat1.add("olma","nok") 
print(food.get_info())
food.food_option()
savat1 = int(input("Siz oziq-ovqat bo'limiga kirdingiz. Tanlang (1-10): "))
print(electronics.get_info())
electronics.elec_option()
savat1 = int(input("Siz electronika bo'limiga kirdingiz. Tanlang (1-10): "))
print(eco.get_info())
eco.ecolo_option()
savat1 = int(input("Siz gigiyena bo'limiga kirdingiz. Tanlang (1-10): "))
print(meal.get_info())
meal.mel_option()
savat1 = int(input("Siz gigiyena bo'limiga kirdingiz. Tanlang (1-10): "))
print(water.get_info())
water.wat_option()
savat1 = int(input("Siz gigiyena bo'limiga kirdingiz. Tanlang (1-10): "))
print(vegfru.get_info())
vegfru.vegfru_option()
savat1 = int(input("Siz gigiyena bo'limiga kirdingiz. Tanlang (1-10): "))
print(candiy.get_info())
candiy.cand_option()
savat1 = int(input("Siz gigiyena bo'limiga kirdingiz. Tanlang (1-10): "))
print(food.choose_food(savat1))  
print(electronics.choose_elec(savat1))  
print(eco.choose_ecolo(savat1)) 
print(meal.choose_mel(savat1)) 
print(water.choose_wat(savat1)) 
print(vegfru.choose_vegfru(savat1)) 
print(candiy.choose_cand(savat1)) 


