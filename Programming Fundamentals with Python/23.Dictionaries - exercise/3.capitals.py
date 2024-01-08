
countries = input().split(", ")
capitals = input().split(", ")

country_capitals = {countries[idx]: capitals[idx] for idx in range(len(countries))}

for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")

# написано горното решение без компрехеншън
# country_capitals = {}
# for idx in range(len(countries)):
#     country = countries[idx]
#     capital = capitals[idx]
#     country_capitals[country] = capital

# countries = input().split(", ")
# capitals = input().split(", ")
#
# country_capitals = [f"{countries[idx]} -> {capitals[idx]}" for idx in range(len(countries))]
# print("\n".join(country_capitals))

# countries = input().split(", ")
# capitals = input().split(", ")
#
# country_capitals = dict(zip(countries, capitals))
# for country, capital in country_capitals.items():
#     print(f"{country} -> {capital}")
