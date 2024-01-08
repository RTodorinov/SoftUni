# import random
#
#
# def guess_the_number(low: int = 1, high: int = 100) -> int:
#     """
#     Plays a guessing game where the user must guess a random number between
#     `low` and `high`. Returns the randomly generated number.
#
#     Args:
#         low (int): The lowest possible number in the range (default 1).
#         high (int): The highest possible number in the range (default 100).
#
#     Returns:
#         int: The randomly generated number.
#
#     """
#     random_number = random.randint(low, high)
#     user_guess = None
#
#     while user_guess != random_number:
#         user_guess = int(input(f"Guess a number between {low} and {high}: "))
#         if user_guess < random_number:
#             print("Your guess is too low. Try again!")
#         elif user_guess > random_number:
#             print("Your guess is too high. Try again!")
#         else:
#             print("Congratulations, you guessed the number correctly!")
#
#     return random_number


import random

random_number = random.randint(1, 100)
user_guess = None

while user_guess != random_number:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess < random_number:
        print("Your guess is too low. Try again!")
    elif user_guess > random_number:
        print("Your guess is too high. Try again!")
    else:
        print("Congratulations, you guessed the number correctly!")
