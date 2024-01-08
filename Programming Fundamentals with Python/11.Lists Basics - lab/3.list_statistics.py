
# n = int(input())
# positives = list()
# negatives = list()
# count_positives = 0
# sum_of_negatives = 0
#
# for n in range(n):
#     number = int(input())
#     if number >= 0:
#         positives.append(number)
#         count_positives += 1
#     else:
#         negatives.append(number)
#         sum_of_negatives += number
#
# print(positives)
# print(negatives)
# print(f"Count of positives: {count_positives}")
# print(f"Sum of negatives: {sum_of_negatives}")

n = int(input())
positives = list()
negatives = list()


for n in range(n):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}.\nSum of negatives: {sum(negatives)}")
