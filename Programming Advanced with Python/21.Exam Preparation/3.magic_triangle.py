def get_magic_triangle(rows):
    result = []
    for row in range(rows):
        result.append([])
        result[row].append(1)
        for col in range(1, row):
            result[row].append(result[row - 1][col - 1] + result[row - 1][col])
        if row != 0:
            result[row].append(1)
    return result
#
#
# print(get_magic_triangle(5))


def get_magic_triangle(n):
    result = []
    result.append([1])
    for i in range(2, n + 1):
        current_result = []
        current_result.append(1)
        last_list = None
        if result and len(result) != 1:
            last_list = result[len(result) - 1]
        if last_list:
            for i in range(0, len(last_list) - 1):
                current_result.append(last_list[i] + last_list[i + 1])
        current_result.append(1)
        result.append(current_result)
    return result


get_magic_triangle(5)
