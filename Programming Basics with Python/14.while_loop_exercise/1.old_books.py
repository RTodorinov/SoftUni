# Ани отива до родния си град след много дълъг период извън страната.
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички книги в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст),
# която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
# •	Ако не открие търсената книгата да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си се отпечатва един ред:
# o	"You checked {брой} books and found it."

searched_book = input()
books_counter = 0

while True:
    current_book = input()
    books_counter += 1
    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_counter -1} books.")
        break

    if searched_book == current_book:
        print(f"You checked {books_counter - 1} books and found it.")
        break

