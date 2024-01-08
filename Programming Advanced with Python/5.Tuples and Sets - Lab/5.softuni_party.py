# import time
# start_time = time.time()

number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    reservation_num = input()
    reservations.add(reservation_num)

guest = input()
while guest != "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))
for reservation_num in sorted(reservations):
    print(reservation_num)

# print("---%s seconds ---" % (time.time() - start_time))
