#  Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
#  С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

trip_price = float(input())

puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

toys_count = puzzles_count + \
             dolls_count + \
             bears_count + \
             minions_count + \
             trucks_count
toys_total_price = (puzzles_count * PUZZLE_PRICE) + \
                   (dolls_count * DOLL_PRICE) + \
                   (bears_count * BEAR_PRICE) + \
                   (minions_count * MINION_PRICE) + \
                   (trucks_count * TRUCK_PRICE)

if toys_count >= 50:
    toys_total_price *= 0.75  # *= 0.75  *= 1 - 0.25  различно разписване на отстъпката
    # отстъпката е 25% от общата цена

toys_total_price *= 0.90  # Взимаме 10% за наема от сумата

if toys_total_price >= trip_price:
    print(f"Yes! {toys_total_price - trip_price:.2f} lv left.")
if toys_total_price < trip_price:
    print(f"Not enough money! {trip_price - toys_total_price:.2f} lv needed.")
