
side_by_user = {}
users_by_side = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        line_arg = line.split(" | ")
        force_side = line_arg[0]
        force_user = line_arg[1]

        if force_side not in users_by_side:
            users_by_side[force_side] = []

        if force_user not in side_by_user:
            side_by_user[force_user] = force_side
            users_by_side[force_side].append(force_user)
    else:
        line_arg = line.split(" -> ")
        force_user = line_arg[0]
        force_side = line_arg[1]

        if force_side not in users_by_side:
            users_by_side[force_side] = []

        users_by_side[force_side].append(force_user)

        if force_user in side_by_user:
            old_side = side_by_user[force_user]
            users_by_side[old_side].remove(force_user)
            side_by_user[force_user] = force_side

        else:
            side_by_user[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")

for side, members in users_by_side.items():
    if len(members) == 0:
        continue
    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
