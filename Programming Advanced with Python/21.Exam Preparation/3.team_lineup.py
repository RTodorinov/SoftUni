def team_lineup(*players_info):

    players_by_country = {}

    for player, country in players_info:
        if country not in players_by_country:
            players_by_country[country] = []
        players_by_country[country].append(player)

    equal_numbers = len(set(len(players) for players in players_by_country.values())) == 1
    if equal_numbers:
        # Sort countries alphabetically if the number of players is equal
        sorted_countries = sorted(players_by_country.items(), key=lambda kvp: (kvp[0], kvp[1]))
    else:
        # Sort countries by the number of players in descending order
        sorted_countries = sorted(players_by_country.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""
    for country, player_ in sorted_countries:
        result += f"{country}:\n"
        for player in player_:
            result += f"  -{player}\n"
    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")
))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
