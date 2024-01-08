
# positive = []
# negative = []
# even = []
# odd = []
# numbers = [int(x) for x in input().split(", ")]
# [even.append(number) if number % 2 == 0 else odd.append(number) for number in numbers]
# [positive.append(number) if number >= 0 else negative.append(number) for number in numbers]
# print(f"Positive: {', '.join(str(number) for number in positive)}")
# print(f"Negative: {', '.join(str(number) for number in negative)}")
# print(f"Even: {', '.join(str(number) for number in even)}")
# print(f"Odd: {', '.join(str(number) for number in odd)}")

# numbers = [int(x) for x in input().split(", ")]
# positive = [x for x in numbers if x >= 0]
# negative = [x for x in numbers if x < 0]
# even = [x for x in numbers if x % 2 == 0]
# odd = [x for x in numbers if x % 2 != 0]
# print("Positive: " + ", ".join(str(x) for x in positive))
# print("Negative: " + ", ".join(str(x) for x in negative))
# print("Even: " + ", ".join(str(x) for x in even))
# print("Odd: " + ", ".join(str(x) for x in odd))


def check_even(nums):
    return [x for x in nums if x % 2 == 0]


def check_odd(nums):
    return [x for x in nums if x % 2 != 0]


def check_positive(nums):
    return [x for x in nums if x >= 0]


def check_negative(nums):
    return [x for x in nums if x < 0]


numbers = [int(x) for x in input().split(", ")]
print("Positive: " + ", ".join(str(x) for x in check_positive(numbers)))
print("Negative: " + ", ".join(str(x) for x in check_negative(numbers)))
print("Even: " + ", ".join(str(x) for x in check_even(numbers)))
print("Odd: " + ", ".join(str(x) for x in check_odd(numbers)))

