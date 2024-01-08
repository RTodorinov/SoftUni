''' Напишете програма, която чете текст от конзолата(стринг) и го принтира, докато не получи командата "Stop". '''

# word = input()
# while word != "Stop":
#     print(word)
#     word = input()
#     if word == "Stop":
#         break

while True:  # по оптимизирано записване от горното с while True
    word = input()
    if word == "Stop":
        break
    print(word)
