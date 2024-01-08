
products_list = input().split("!")
data_info = input()

while data_info != "Go Shopping!":

    command, *info = data_info.split()
    if command == "Correct":
        old_item, new_item = info
        if old_item in products_list:
            products_list[products_list.index(old_item)] = new_item
        data_info = input()
        continue

    item = info[0]

    if command == "Urgent":
        if item not in products_list:
            products_list.insert(0, item)

    elif command == "Unnecessary":
        if item in products_list:
            products_list.remove(item)

    elif command == "Rearrange":
        if item in products_list:
            # products_list.remove(item)
            # products_list.append(item)
            products_list.append(products_list.pop(products_list.index(item)))

    data_info = input()

print(", ".join(products_list))
