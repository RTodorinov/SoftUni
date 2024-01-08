# Басейн с обем V има две тръби от които се пълни.
# Всяка тръба има определен дебит (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа.
# Напишете програма, която изкарва състоянието на басейна, в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# "The pool is {запълненост на басейна в проценти}% full.
# Pipe 1: {процент вода от първата тръба}%. Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# "For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."

# Volume of the pool
V = int(input())
# Flow rate of the first pipe
P1 = int(input())
# Flow rate of the second pipe
P2 = int(input())
# Hours the worker is absent
H = float(input())

# Total flow rate
total_flow_rate = P1 + P2
# Water filled in the pool
water_filled = total_flow_rate * H

# Pool is overflowing
if water_filled > V:
    overflow = water_filled - V
    print(f"For {H} hours the pool overflows with {overflow} liters.")
else:
    # Percentage filled in the pool
    percent_filled = (water_filled / V) * 100
    # Percentage from first pipe
    percent_from_pipe_1 = (P1 / total_flow_rate) * 100
    # Percentage from second pipe
    percent_from_pipe_2 = 100 - percent_from_pipe_1
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {percent_from_pipe_1:.2f}%. Pipe 2: {percent_from_pipe_2:.2f}%.")
