
def loading_number(some_number):

    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percent = some_number // 10
    return f"{some_number}% [{'%' * percent}{'.' * (10 - percent)}]\nStill loading..."


number = int(input())
print(loading_number(number))
