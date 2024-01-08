
gifts = input().split()
while True:
    line = input()
    if line == "No Money":
        break
    line_args = line.split()
    command = line_args[0]
    gift = line_args[1]

    if command == "OutOfStock":
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"
    elif command == "Required":
        idx = int(line_args[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift
    elif command == "JustInCase":
        gifts[-1] = gift

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=" ")

''' This code is a basic implementation of a gift management system. Let's go through it step by step:
gifts = input().split(): This line takes user input and splits it into a list of strings. 
Each string represents a gift. The input should be provided in a single line, with gift names separated by spaces.

while True:
: This line initiates an infinite loop, which means the following code block 
will keep executing until a specific condition is met.
line = input(): This line takes user input and assigns it to the variable line. 
This input represents a command or action related to gift management.
if line == "No Money": break: This line checks if the input is equal to the string "No Money". 
If it is, the break statement is executed, which terminates the infinite loop, effectively ending the program.
line_args = line.split(): This line splits the input line into a list of strings, using whitespace as the delimiter. 
The resulting list is stored in the variable line_args.
command = line_args[0] and gift = line_args[1]: These lines extract the first and second elements from the 
line_args list and assign them to the variables command and gift, respectively. 
The command variable represents the type of action to be performed (e.g., "OutOfStock", "Required", "JustInCase"), and 
the gift variable represents the name of the gift associated with that action.

The code then proceeds to check the value of the command variable using conditional statements (if, elif, else) to 
determine which action to perform.
If command == "OutOfStock", the code enters the first conditional block. It iterates over the gifts list using a 
for loop and checks if each gift is equal to the gift variable. 
If a match is found, that gift is replaced with the string "None".
If command == "Required", the code enters the second conditional block. It retrieves an index value from line_args 
(the third element, line_args[2]), converts it to an integer, and assigns it to the variable idx. It then checks if the 
index value is within the valid range of the gifts list and, if so, 
replaces the gift at that index with the gift variable.
If command == "JustInCase", the code enters the third conditional block. It assigns the gift variable to the last 
element of the gifts list, effectively replacing it.
After executing the action based on the command, the loop goes back to the beginning and prompts for the next command 
until the "No Money" command is entered.
Once the loop is terminated, the code proceeds to the next block outside the loop.
The for loop iterates over each gift in the gifts list. If a gift is equal to the string "None", it continues to the 
next iteration, skipping the rest of the loop. Otherwise, it prints the gift followed by a space, using the end 
parameter to ensure the gifts are printed on the same line.
Finally, the program ends, and the printed gifts are displayed as output.
This code allows the user to manage a list of gifts by performing actions such as marking a gift as out of stock, 
replacing a gift at a specific index, or updating the last gift. It then prints the updated list of gifts, 
excluding any gifts marked as "None". '''