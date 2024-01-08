from collections import deque

quantity_of_food = int(input())
orders_queue = deque([int(x) for x in input().split()])

print(max(orders_queue))

while orders_queue and orders_queue[0] <= quantity_of_food:
    quantity_of_food -= orders_queue[0]
    orders_queue.popleft()

if orders_queue:
    print(f'Orders left:', end='')
    while orders_queue:
        print(f' {orders_queue.popleft()}', end='')
else:
    print("Orders complete")

# from collections import deque
#
# quantity_of_food = int(input())
# orders_queue = deque([int(x) for x in input().split()])
#
# print(max(orders_queue))
#
# while orders_queue and orders_queue[0] <= quantity_of_food:
#     quantity_of_food -= orders_queue.popleft()
#
# if orders_queue:
#     print(f'Orders left:', end='')
#     while orders_queue:
#         print(f' {orders_queue.popleft()}', end='')
# else:
#     print("Orders complete")
