#  Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко
#  ще е часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
#  а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две
#  цифри, с водеща нула, когато е необходимо.

hours = int(input())
minutes = int(input()) + 15
# ползват се два пъти if за да са независими проверките на minutes и hours.
if minutes > 59:   # ако това е вярно изпълняваме долните редове.
    hours += 1     # добавяме един час към часовете защото минутите са прескочили над 59.
    minutes -= 60  # премахваме стойноста на един час за да получим оставащите минути.

if hours > 23:
    hours -= 24    # премахваме стойноста на един ден за да нулираме както горе с минутите.

print(f"{hours}:{minutes:02d}")
