# Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
# като имате предвид следната таблица:
# Градуси	Време
#  26.00 - 35.00	Hot
#  20.1 - 25.9	    Warm
#  15.00 - 20.00	Mild
#  12.00 - 14.9	    Cool
#  5.00 - 11.9	    Cold
#  Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".

degrees = float(input())

if degrees == 5.00:
    print("Cold")
elif degrees <= 11.9:
    print("Cold")
elif degrees == 12.00:
    print("Cool")
elif degrees <= 14.9:
    print("Cool")
elif degrees == 15.00:
    print("Mild")
elif degrees <= 20.00:
    print("Mild")
elif degrees == 20.1:
    print("Warm")
elif degrees <= 25.9:
    print("Warm")
elif degrees == 26:
    print("Hot")
elif degrees <= 35.00:
    print("Hot")
else:
    print("unknown")
