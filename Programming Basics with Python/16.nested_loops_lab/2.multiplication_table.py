# Отпечатайте на конзолата таблицата за умножение за числата от 1 до 10 във формат:
# "{първи множител} * {втори множител} = {резултат}".

for a in range(1, 11):
    for b in range(1, 11):
        result = a * b
        print(f"{a} * {b} = {result}")
