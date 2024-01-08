chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

menus_price = (chicken_menu * CHICKEN_MENU_PRICE) +\
              (fish_menu * FISH_MENU_PRICE) +\
              (vegetarian_menu * VEGETARIAN_MENU_PRICE)
desert_price = menus_price * 0.20
total_price = menus_price + desert_price + DELIVERY_PRICE

print(f"{total_price}")
