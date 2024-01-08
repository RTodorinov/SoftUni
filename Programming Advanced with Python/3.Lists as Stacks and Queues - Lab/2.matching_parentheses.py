string = input()
stack = []

for idx in range(len(string)):
    if string[idx] == "(":
        stack.append(idx)
    elif string[idx] == ")":
        start_idx = stack.pop()
        last_index = idx + 1
        print(string[start_idx:last_index])  # when we use slicing second element is exclusive
