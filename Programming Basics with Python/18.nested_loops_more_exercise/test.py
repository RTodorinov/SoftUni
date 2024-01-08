import string

n_number = int(input())
l_number = int(input())

for n_one in range(1, n_number):
    for n_num in range(1, n_number):
        for l_tree in string.ascii_lowercase[:l_number]:
            for l_four in string.ascii_lowercase[:l_number]:
                for check in range(1, n_number + 1):
                    if n_one < check and check > n_num and check <= n_number:
                        print(f"{n_one}{n_num}{l_tree}{l_four}{check}", end=" ")
