from collections import deque

initial_fuel = list(map(int, input().split()))
consumption_indexes = deque(map(int, input().split()))
needed_fuel = list(map(int, input().split()))

altitudes_reached = []
failed_to_reach = False

altitude_index = 1

while initial_fuel and needed_fuel:
    current_fuel = initial_fuel.pop()
    consumption_index = consumption_indexes.popleft()
    altitude_fuel = needed_fuel[0]

    result = current_fuel - consumption_index

    if result >= altitude_fuel:
        altitudes_reached.append(altitude_index)
        needed_fuel.pop(0)
        print(f"John has reached: Altitude {altitude_index}")
    else:
        failed_to_reach = True
        print(f"John did not reach: Altitude {altitude_index}")
        break

    altitude_index += 1

if not altitudes_reached:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif failed_to_reach:
    remaining_altitudes = [index for index in range(altitude_index, altitude_index + len(needed_fuel))]
    print("John failed to reach the top.")
    print("Reached altitudes: " + ", ".join([f"Altitude {index}" for index in altitudes_reached]))
else:
    print("John has reached all the altitudes and managed to reach the top!")
