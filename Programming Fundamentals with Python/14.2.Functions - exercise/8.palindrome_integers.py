
def check_palindrome(num):
    if num == num[::-1]:
        return True
    return False


numbers = input().split(", ")
for number in numbers:
    print(check_palindrome(number))
