def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result  # [next(seq) for _ in range(n)]  #  [item for item, _ in zip(seq, range(n))]

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print("------------------")

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
