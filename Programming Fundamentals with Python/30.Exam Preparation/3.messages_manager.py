def manage_messages(capacity):
    users = {}
    insertion_order = []

    while True:
        command = input().strip()
        if command == "Statistics":
            break

        command_parts = command.split("=")
        action = command_parts[0]

        if action == "Add":
            username = command_parts[1]
            sent_messages = int(command_parts[2])
            received_messages = int(command_parts[3])

            if username not in users:
                users[username] = {'sent': sent_messages, 'received': received_messages}
                insertion_order.append(username)

        elif action == "Message":
            sender = command_parts[1]
            receiver = command_parts[2]

            if sender in users and receiver in users:
                users[sender]['sent'] += 1
                users[receiver]['received'] += 1

                if users[sender]['sent'] + users[sender]['received'] >= capacity:
                    del users[sender]
                    print(f"{sender} reached the capacity!")
                    insertion_order.remove(sender)

                if users[receiver]['sent'] + users[receiver]['received'] >= capacity:
                    del users[receiver]
                    print(f"{receiver} reached the capacity!")
                    insertion_order.remove(receiver)

        elif action == "Empty":
            username = command_parts[1]

            if username == "All":
                users.clear()
                insertion_order.clear()
            elif username in users:
                del users[username]
                insertion_order.remove(username)

    print(f"Users count: {len(users)}")
    for username in insertion_order:
        messages = users[username]
        total_messages = messages['sent'] + messages['received']
        print(f"{username} - {total_messages}")


if __name__ == "__main__":
    capacity = int(input())
    manage_messages(capacity)

''' 
def manage_messages(capacity):
We start by defining the main function manage_messages, which takes the capacity as an argument. 
This function will manage the user records and messages.
users is a dictionary that will store the user information, with usernames as keys and dictionaries containing their
sent and received messages as values.
insertion_order is a list that will keep track of the order in which users were added to the users dictionary.

while True:
        command = input().strip()
        if command == "Statistics":
            break
This sets up an infinite loop to keep receiving commands from the user until the command "Statistics" is encountered. 
When "Statistics" is input, the loop will break, and the program will proceed to print the results.

command_parts = command.split("=")
        action = command_parts[0]
This line splits the input command into parts using the "=" as a separator. 
The first part will represent the action to be performed ("Add", "Message", or "Empty").

if action == "Add":
            username = command_parts[1]
            sent_messages = int(command_parts[2])
            received_messages = int(command_parts[3])

            if username not in users:
                users[username] = {'sent': sent_messages, 'received': received_messages}
                insertion_order.append(username)
If the action is "Add", the program extracts the username, sent_messages, and received_messages from the command.
If the username is not already in the users dictionary, the program creates a new entry for that user with their sent 
and received messages.
It also adds the username to the insertion_order list to keep track of the order in which users were added.

elif action == "Message":
            sender = command_parts[1]
            receiver = command_parts[2]

            if sender in users and receiver in users:
                users[sender]['sent'] += 1
                users[receiver]['received'] += 1

                if users[sender]['sent'] + users[sender]['received'] >= capacity:
                    del users[sender]
                    print(f"{sender} reached the capacity!")
                    insertion_order.remove(sender)

                if users[receiver]['sent'] + users[receiver]['received'] >= capacity:
                    del users[receiver]
                    print(f"{receiver} reached the capacity!")
                    insertion_order.remove(receiver)
If the action is "Message", the program extracts the sender and receiver usernames from the command.
It checks if both sender and receiver are present in the users dictionary.
If they are, the program increases the sent count for the sender and the received count for the receiver.
It then checks if either the sender or the receiver has reached or exceeded the capacity. 
If so, it removes the corresponding user from the users dictionary and prints a message that 
the user has reached the capacity.
It also removes the user from the insertion_order list to maintain the exact order of users in the output.

elif action == "Empty":
            username = command_parts[1]

            if username == "All":
                users.clear()
                insertion_order.clear()
            elif username in users:
                del users[username]
                insertion_order.remove(username)
If the action is "Empty", the program extracts the username from the command.
If the username is "All", it clears all user records in the users dictionary and also empties the insertion_order list.
If the username is present in the users dictionary, it deletes the user's record and removes
the user from the insertion_order list.

print(f"Users count: {len(users)}")
    for username in insertion_order:
        messages = users[username]
        total_messages = messages['sent'] + messages['received']
        print(f"{username} - {total_messages}")
After processing all commands, the program prints the total count of users remaining in the users dictionary.
It then iterates through the insertion_order list to print the usernames in the order they were added.
For each user, it calculates the total number of messages and prints the username along with the total message count.

if __name__ == "__main__":
    capacity = int(input())
    manage_messages(capacity)
Finally, the program checks if it is being run as the main module and reads the capacity input from the user.
It then calls the manage_messages function with the provided capacity to start the message management process.

'''