from collections import deque
command = input()
queue = deque()

while command != "End":
    if command == "Paid":
        while len(queue):
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")

# from collections import deque
# queue = deque()
# while True:
#     command = input()
#     if command == "Paid":
#         while len(queue):
#             print(queue.popleft())
#     elif command == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     else:
#         queue.append(command)
