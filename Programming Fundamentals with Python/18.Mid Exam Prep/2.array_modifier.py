nums = [int(x) for x in input().split()]
data_info = input()

while data_info != "end":
    if "decrease" in data_info:
        # for i in range(len(elements)):
        #     elements[i] -= 1
        nums = [x - 1 for x in nums]
        data_info = input()
        continue
    # current_list = data_info.split()
    # current_list[0] == "swap"
    # index_1, index_2 = int(current_list[1]), int(current_list[2])
    # nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
    command, index_one, index_two = [x if x.isalpha() else int(x) for x in data_info.split()]

    if command == "swap":
        nums[index_one], nums[index_two] = nums[index_two], nums[index_one]
    elif command == "multiply":
        nums[index_one] *= nums[index_two]

    data_info = input()
print(*nums, sep=", ")
