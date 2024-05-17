import random
number_of_streaks = 0
for experiment_number in range(10000):
    results = []
    for i in range(100):
        results.append(random.randint(0, 1))
    for i in range(95):
        if results[i] == results[i + 1] == results[i + 2] == results[i + 3] == results[i + 4] == results[i + 5]:
            number_of_streaks += 1
            break
print(f'同じ面が6回連続で出現する確率。{number_of_streaks / 100}%')

