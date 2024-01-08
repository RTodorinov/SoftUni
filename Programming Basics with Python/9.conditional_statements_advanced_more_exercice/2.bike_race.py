# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors")
# и старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите.
# Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Група	        trail	   cross-country	downhill	road
# juniors	    5.50	   8	            12.25	    20
# seniors	    7	       9.50	            13.75	    21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.

junior_bikers = int(input())
senior_bikers = int(input())
race_type = input()

bikers_total = junior_bikers + senior_bikers
donation_sum = 0

if race_type == "cross-country":
    if bikers_total >= 50:
        donation_sum = ((junior_bikers * 8) + (senior_bikers * 9.50)) * 0.75
        donation_sum *= 0.95
    else:
        donation_sum = (junior_bikers * 8) + (senior_bikers * 9.50)
        donation_sum *= 0.95
elif race_type == "trail":
    donation_sum = (junior_bikers * 5.50) + (senior_bikers * 7)
    donation_sum *= 0.95
elif race_type == "downhill":
    donation_sum = (junior_bikers * 12.25) + (senior_bikers * 13.75)
    donation_sum *= 0.95
elif race_type == "road":
    donation_sum = (junior_bikers * 20) + (senior_bikers * 21.50)
    donation_sum *= 0.95

print(f"{donation_sum:.2f}")
