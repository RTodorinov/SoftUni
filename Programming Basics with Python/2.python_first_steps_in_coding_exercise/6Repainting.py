nylon = int(input())
paint = int(input())
paint_diluent = int(input())
work_hours = int(input())

NYLON_PRICE = 1.50
PAINTING_PRICE = 14.50
PAINT_DILUENT_PRICE = 5.00
BAG_PRICE = 0.40

# nylon = nylon + nylon + 2
nylon += 2
# paint = paint + paint * 0.10
paint += paint * 0.10

material_price = (nylon * NYLON_PRICE) +\
                 (paint * PAINTING_PRICE) +\
                 (paint_diluent * PAINT_DILUENT_PRICE) + BAG_PRICE
price_for_hour_work = (material_price * 0.30) * work_hours
total_sum = material_price + price_for_hour_work

print(total_sum)
