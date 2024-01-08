
numbers = [int(x) for x in input().split(", ")]
#  numbers = list(map(int, input().split(", "))

found_index_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
even_index = list(filter(lambda x: x != "no", found_index_or_no))
print(even_index)
