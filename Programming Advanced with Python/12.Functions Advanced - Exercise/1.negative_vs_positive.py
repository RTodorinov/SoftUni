# def nums_sums(*args):
#     neg_sum = 0
#     pos_sum = 0
#     for num in args:
#         if num > 0:
#             pos_sum += num
#         else:
#             neg_sum += num
#
#     return neg_sum, pos_sum
#
#
# nums = [int(x) for x in input().split()]
#
# print(nums_sums(*nums)[0])
# print(nums_sums(*nums)[1])
# if abs(nums_sums(*nums)[0]) > nums_sums(*nums)[1]:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


# def negative_vs_positive(data):
#     min_number = data.index(min([x for x in data if x > 0])) # O(n) + O(n) , ind 0(1)
#     positive_numbers = sum(data[min_number:]) # O(k+n)
#     negative_numbers = sum(data[:min_number]) # O(k+n)
#
#     if positive_numbers > abs(negative_numbers):
#         text = "The positives are stronger than the negatives"
#     else:
#         text = "The negatives are stronger than the positives"
#     return f"{negative_numbers}\n{positive_numbers}\n{text}"
#
#
# input_numbers = sorted(int(x) for x in input().split()) # O(n log n)
# print(negative_vs_positive(input_numbers))


def negative_vs_positive(data):
    positive_numbers = 0
    negative_numbers = 0
    for num in data:
        if num > 0:
            positive_numbers += num
        else:
            negative_numbers += num

    if abs(negative_numbers) > positive_numbers:
        text = "The negatives are stronger than the positives"
    else:
        text = "The positives are stronger than the negatives"
    return f"{negative_numbers}\n{positive_numbers}\n{text}"


input_numbers = [int(x) for x in input().split()]
print(negative_vs_positive(input_numbers))
