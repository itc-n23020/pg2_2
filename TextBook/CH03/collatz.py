def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

number = int(input("整数を入力してください: "))
sequence = collatz(number)
for num in sequence:
    print(num)

