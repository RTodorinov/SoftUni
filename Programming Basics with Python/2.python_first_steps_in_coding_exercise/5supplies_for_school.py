pens_packs = int(input())
marker_packs = int(input())
detergent_packs = int(input())
discount = int(input()) / 100

PENS_PAKET_PRICE = 5.80
MARKER_PAKET_PRICE = 7.20
DETERGENT_LITER_PRICE = 1.20

total_price = (pens_packs * PENS_PAKET_PRICE) +\
              (marker_packs * MARKER_PAKET_PRICE) +\
              (detergent_packs * DETERGENT_LITER_PRICE)
final_price = total_price - (total_price * discount)

print(final_price)







