from collections import deque

worms = [int(el) for el in input().split()]
holes = deque([int(el) for el in input().split()])

matches_count = 0
len_holes = len(holes)

while worms and holes:
    current_hole = holes.popleft()
    current_worm = worms.pop()

    if current_worm == current_hole:
        matches_count += 1
    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

if matches_count > 0:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if not worms:
    if matches_count == len_holes:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
