
animals = input().split(', ')
if animals[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    sheep_index = len(animals) - animals.index('wolf') - 1
    print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")

''' This code takes the input of the animals as a string and splits it into a list using the comma and space as 
the separator. Then it checks if the last animal in the list is a wolf. 
If it is, it prints the message "Please go away and stop eating my sheep". 
Otherwise, it finds the index of the wolf in the list, subtracts it from the length of the list, and subtracts 1 to 
get the position of the sheep that is about to be eaten. 
Finally, it prints the message "Oi! Sheep number N! You are about to be eaten by a wolf!", where N is the 
sheep's position in the queue. '''

sheeps = list(reversed(input().split(', ')))
print('Please go away and stop eating my sheep'
      if sheeps[0] == 'wolf' else f'Oi! Sheep number {sheeps.index("wolf")}! You are about to be eaten by a wolf!')
