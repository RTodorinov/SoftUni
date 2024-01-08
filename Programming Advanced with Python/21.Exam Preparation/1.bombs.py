from collections import deque

bombs_effects = deque(int(x) for x in input().split(', '))
bombs_casing = [int(x) for x in input().split(', ')]
full_set = False

bombs = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

while not full_set and bombs_casing and bombs_effects:
    effect = bombs_effects.popleft()
    casing = bombs_casing.pop()
    mix_effect = effect + casing

    for bomb, quantity in (('Datura Bombs', 40), ('Cherry Bombs', 60), ('Smoke Decoy Bombs', 120)):
        if mix_effect == quantity:
            bombs[bomb] += 1
            break
    else:
        bombs_casing.append(casing - 5)
        bombs_effects.appendleft(effect)
        continue

    if all(x >= 3 for x in bombs.values()):
        full_set = True

if full_set:
    set_result = "Bene! You have successfully filled the bomb pouch!"
else:
    set_result = "You don't have enough materials to fill the bomb pouch."
print(set_result)

if bombs_effects:
    bomb = f"Bomb Effects: {', '.join(str(x) for x in bombs_effects)}"
else:
    bomb = "Bomb Effects: empty"
print(bomb)

if bombs_casing:
    casing_bomb = f"Bomb Casings: {', '.join(str(x) for x in bombs_casing)}"
else:
    casing_bomb = f"Bomb Casings: empty"
print(casing_bomb)

for bomb, quantity in bombs.items():
    print(f"{bomb}: {quantity}")
