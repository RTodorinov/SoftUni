# brute force атака

import random, pyautogui, string

digits = list(string.digits)
iteration_counter = 0
password = input("Enter your pin code here: ")

guess_password = ""

while guess_password != password:
    guess_password = random.choices(digits, k=len(password))
    iteration_counter += 1
    print(f">>>{''.join(guess_password)}<<<")

    if guess_password == list(password):
        print(f"Your pin code is: {''.join(guess_password)}\n"
              f"Number of iteration counter is: {iteration_counter}")
        break
