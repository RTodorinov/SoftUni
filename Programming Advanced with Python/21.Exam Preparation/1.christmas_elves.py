'''
1. Reading two sequences - deque
2. While we have elves and materials
 - First elf
 - Last material
3. Check if elf is with energy less than 5
  - remove the elf and don't count it as iteration
4. Increment iterations
5. Check if elf is on iteration 3
 - double the material and double the count of toys that are created
6. Check if elf has energy to create the toy
 - update the total amount of materials
 - decrease elf energy
 - update total used energy
 - give cookie to the elf (increase elf energy by 1)
 - check if iteration is 5 (don't give cookie and decrease energy by 1)
   - current_toys_count is 0
7. Add toys to total count
8. Append elf at the end of the list
9. print values
'''

from collections import deque

elves_energy = deque([int(el) for el in input().split()])
materials_in_box = deque([int(el) for el in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elves_energy and materials_in_box:
    elf = elves_energy.popleft()
    material = materials_in_box[-1]

    if elf < 5:
        continue

    iterations += 1
    current_toys_count = 0

    if iterations % 3 == 0:
        material *= 2
        current_toys_count += 1

    if elf >= material:
        total_energy += material
        elf -= material

        if iterations % 5 != 0:
            elf += 1
            current_toys_count += 1
        else:
            current_toys_count = 0

        materials_in_box.pop()
    else:
        elf *= 2
        current_toys_count = 0

    total_toys += current_toys_count
    elves_energy.append(elf)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")
