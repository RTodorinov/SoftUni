
# cards = input().split()
# team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# is_terminate = False
# for card in cards:
#     card_arg = card.split("-")
#     team = card_arg[0]
#     player_number = int(card_arg[1])
#
#     if team == "A":
#         if player_number in team_a:
#             team_a.remove(player_number)
#     elif team == "B":
#         if player_number in team_b:
#             team_b.remove(player_number)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         is_terminate = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if is_terminate:
#     print("Game was terminated")

# cards = input().split()
# first_team = []
# second_team = []
#
# should_terminate = False
# for card in cards:
#     if card in first_team or card in second_team:
#         continue
#
#     card_args = card.split("-")
#     team_name = card_args[0]
#     player_number = card_args[1]
#
#     is_first_team = team_name == "A"  # True or False
#     if is_first_team:
#         first_team.append(card)
#     else:
#         second_team.append(card)
#     if len(first_team) > 4 or len(second_team) > 4:
#         should_terminate = True
#         break
#
# print(f"Team A - {11 - len(first_team)}; Team B - {11 - len(second_team)}")
# if should_terminate:
#     print("Game was terminated")

info = input().split()
team_a_players = 11
team_b_players = 11
player_loses = []
condition = False

for card in info:
    if card not in player_loses:
        player_loses.append(card)
        if "A" in card:
            team_a_players -= 1
        elif "B" in card:
            team_b_players -= 1
        if team_a_players < 7 or team_b_players < 7:
            condition = True
            break
print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if condition:
    print("Game was terminated")

# red_cards = input().split()
# removed_players_a = []
# removed_players_b = []
#
# should_terminate = False
# for card in red_cards:
#     if card in removed_players_a or card in removed_players_b:
#         continue
#
#     card_arg = card.split("-")
#     if card_arg[0] == "A":
#         removed_players_a.append(card)
#     else:
#         removed_players_b.append(card)
#     if len(removed_players_a) > 4 or len(removed_players_b) > 4:
#         should_terminate = True
#         break
#
# print(f"Team A - {11 - len(removed_players_a)}; Team B - {11 - len(removed_players_b)}")
# if should_terminate:
#     print("Game was terminated")
