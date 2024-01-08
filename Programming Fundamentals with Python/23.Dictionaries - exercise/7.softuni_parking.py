
registrations_by_username = {}
count = int(input())
for _ in range(count):
    command_args = input().split()
    command = command_args[0]
    name = command_args[1]

    if command == "register":
        license_plate = command_args[2]
        if name in registrations_by_username:
            print(f"ERROR: already registered with plate number {registrations_by_username[name]}")
        else:
            registrations_by_username[name] = license_plate
            print(f"{name} registered {registrations_by_username[name]} successfully")

    else:
        if name in registrations_by_username:
            registrations_by_username.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for user, license_number in registrations_by_username.items():
    print(f"{user} => {license_number}")
