# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече.
# Минутите винаги печатайте с 2 цифри, например "1:03”.

exam_hour = int(input())
exam_minutes = int(input())

student_hour_arrival = int(input())
student_minutes_arrival = int(input())

exam_time_in_minutes = exam_minutes + exam_hour * 60
student_time_in_minutes = student_minutes_arrival + student_hour_arrival * 60

time_diff = exam_time_in_minutes - student_time_in_minutes  # 630 - 600 = 30 minutes
# 0 - 30 min => On time, 30+ => Early, -number => Late
if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")

hours = 0
minutes = abs(time_diff)
result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"
print(result)
