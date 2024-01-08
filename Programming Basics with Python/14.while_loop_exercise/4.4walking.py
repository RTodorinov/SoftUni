GOAL = 10000
today_steps = 0
going_home = False

while True:
    steps = input()
    if steps == "Going home":
        going_home = True
    else:
        today_steps += int(steps)
        if today_steps >= GOAL:
            print("Goal reached! Good job!")
            print(f"{today_steps - GOAL} steps over the goal!")
            break
        elif going_home:
            print(f"{(GOAL - today_steps)} more steps to reach goal.")
            break
