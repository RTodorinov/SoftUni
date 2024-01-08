for _ in range(5):
    username = input("Enter username: ")
    if username == "Admin":
        print("Welcome")
        break
else:
    print("Wrong username")
