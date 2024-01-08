text = input()

try:
    n_times = int(input())
    for _ in range(n_times):
        print(text, end='')
except ValueError:
    print("Variable times must be an integer")
