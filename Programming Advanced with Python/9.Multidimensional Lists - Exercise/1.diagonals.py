n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")


# n = int(input())  # size of matrix
# matrix = []
# for _ in range(n):  # fill up matrix
#     matrix.append([int(x) for x in input().split(', ')])
#
# primary_diagonal = [matrix[i][i] for i in range(n)]  # getting diagonals by index
# secondary_diagonal = [matrix[i][- i - 1] for i in range(n)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
