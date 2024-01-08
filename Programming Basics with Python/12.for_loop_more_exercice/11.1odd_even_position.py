import sys

n = int(input())
OddSum = 0
EvenSum = 0
OddMin = sys.maxsize
OddMax = -sys.maxsize
EvenMin = sys.maxsize
EvenMax = -sys.maxsize
for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        EvenSum += num
        if num > EvenMax:
            EvenMax = num
        if num < EvenMin:
            EvenMin = num
    else:
        OddSum += num
        if num > OddMax:
            OddMax = num
        if num < OddMin:
            OddMin = num
print(f"OddSum={OddSum:.2f},")
if OddMin != sys.maxsize:
    print(f"OddMin={OddMin:.2f},")
else:
    print("OddMin=No,")
if OddMax != -sys.maxsize:
    print(f"OddMax={OddMax:.2f},")
else:
    print("OddMax=No,")
print(f"EvenSum={EvenSum:.2f},")
if EvenMin != sys.maxsize:
    print(f"EvenMin={EvenMin:.2f},")
else:
    print("EvenMin=No,")
if EvenMax != -sys.maxsize:
    print(f"EvenMax={EvenMax:.2f}")
else:
    print("EvenMax=No")