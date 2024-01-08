lenght = int(input())
width = int(input())
height = int(input())
percent_filled = float(input()) / 100

volume = lenght * width * height / 1000
# volume = volume * (1 - percent_filled)
# volume = volume - volume * percent_filled
volume -= volume * percent_filled

print(volume)
