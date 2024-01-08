budget = float(input("Enter budget: "))
season = input("Enter season (Summer or Winter): ")

location = ""
accommodation = ""
price = 0.0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6
else:
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.9
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.9

print("{} - {} - {:.2f}".format(location, accommodation, price))
