
# стринга се обхожда с индекс но е непроменяем(unmutable)
word = "Hello"
word += "!"
print(word)  # това се записва на ново място в паметта а не променя първия запис

#  компютрите разбират стринговете чрез бинарна система и уникод, аски код,
#  string се огражда с единични кавички или двойни.

# String Manipulations
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

str1 = "red"
print(str1 * 3)

# String Formating
x = "apples"
y = "lemons"
z = "In the basket are %s and %s" % (x, y)
print(z)

x = "apples"
y = "lemons"
z = "In the basket are {} and {}" .format(x, y)
print(z)

x = "apples"
y = "lemons"
z = f"In the basket are {x} and {y}"
print(z)


# slicing се ползва при стрингове, листове
# когато слайсваме копираме данните и ги слайсваме
# слайсинга върви винаги от ляво на дясно освен ако нямаме трети аргумент за стъпка с -1
print("Hello")
print("Hello"[0:3])
print("Hello"[1:4])
print("Hello"[:])
print("Hello"[::-1])
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[0:6:2]  # range(0, len(a), 2)
# b = a[-6:]
# b = a[::-1]
print(b)
result = [1, 2, 3, [100, 200, 300], 5, 6, 7, 8]
print(result[-5])
print(result[-5][::-1])
text = "My name is Peter"
name = text[-len(text):-6]
print(name)


# String Methods
# там където проверява за големи, малки букви цифрите и символите не играят никаква роля

print("1".isdigit())  # проверява дали стринга е число
print("pe".islower())  # проверява дали в стринга всички букви са малки
print("PA".isupper())  # проверява дали в стринга всички букви са големи
print("a".isalpha())  # проверява дали в стринга всички са букви
print("а2".isalnum())  # проверява дали в стринга всички са или букви или цифри или и двете
print("s".isascii())  # проверява дали в стринга всички са от ascii таблицата
print("3".isdecimal())  # проверява дали стринга са числа

# обръща целия стринг в главни букви
test = "hello".upper()
print(test)

# обръща целия стринг в малки букви
test = "HeLLo".lower()
print(test)

# премахва празните пространства отпред/отзад или изцяло от стринга
# може да премахваме и други неща .strip("!")
print(" hello ".lstrip())
print(" hello ".rstrip())
print(" hello ".strip())

# смяна на всички местоположения на дадена дума/буква с друга дума/буква

# смена bananas с apples 2 пъти в текста
txt = "I like bananas bananas bananas"
x = txt.replace("bananas", "apples", 2)
print(x)

# сменя бананите колкото пъти ги види в текста с ябълки
txt = "I like bananas"
print(txt.replace("bananas", "apples"))
