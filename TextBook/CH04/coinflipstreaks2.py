from random import randint

count = sum(
    any(sum(randint(0, 1) for _ in range(6)) in {0, 6} for _ in range(94))
    for _ in range(10000))

p = count / 10000
print(f'同じ面が6回連続で出現する確率: {p}%')
