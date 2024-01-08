# Котката Том обича по цял ден да спи, за негово съжаление стопанинът му си играе с него
# винаги когато  има свободно време. За да се наспи добре, нормата за игра на Том е 30 000  минути в година.
# Времето за игра на Том зависи от почивните дни на стопанина му:
# •	Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# •	Когато почива, стопанинът му си играе с него  по 127 минути на ден.
# Напишете програма, която въвежда броя почивни дни и отпечатва дали
# Том може да се наспи добре и колко е разликата от нормата за текущата година, като приемем че годината има 365 дни.
# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 345).
# Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.
# Вход
# Входът се чете от конзолата и се състои от едно число – броят почивни дни – цяло число в интервала [0...365]
# Изход
# На конзолата трябва да се отпечатат два реда.
# •	Ако времето за игра на Том е над нормата за текущата година:
# o	 На първия ред отпечатайте: “Tom will run away”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes more for play”
# •	Ако времето за игра на Том е под нормата за текущата година:
# o	На първия ред отпечатайте: “Tom sleeps well”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes less for play”

PLAY_NORM = 30000
WORK_MINUTES = 63
OFF_MINUTES = 127

number_of_days_off = int(input())

real_time_for_play = (365 - number_of_days_off) * WORK_MINUTES + number_of_days_off * OFF_MINUTES
diff_norm_play = PLAY_NORM - real_time_for_play

hours = ""
minutes = abs(diff_norm_play)

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if diff_norm_play > 0:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
