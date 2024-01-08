n_line_queries = int(input())
stack = []
for _ in range(n_line_queries):
    query = input().split()
    if query[0] == "1":
        stack.append(int(query[1]))
    elif stack:  # трябва да се провери дали има нещо в стака за да не даде грешка
        if query[0] == "2":
            stack.pop()
        elif query[0] == "3":
            print(max(stack))
        elif query[0] == "4":
            print(min(stack))

while stack:
    print(stack.pop(), end='')
    if stack:  # ако все още има неща в стака тогава сложи запетайка и интервал.
        print(', ', end='')
