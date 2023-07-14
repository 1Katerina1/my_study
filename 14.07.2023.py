'''
    Hexlet: Реализуйте функцию is_perfect(),
    которая принимает число и возвращает True,
    если оно совершенное, и False — в ином случае.

    Совершенное число — это положительное целое число,
    равное сумме его положительных делителей (не считая само число).
    Например, 6 — совершенное число, потому что 6 = 1 + 2 + 3.

    is_perfect(6)  # True
    is_perfect(1)  # False
'''

# Мое решение:
def is_perfect(number):
    if number <= 0:
        return False
    else:
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        if sum == number:
            return True
        return False

# Решение учителя:
def is_perfect(number):
    if number < 6:
        return False

    limit = number // 2 + 1
    sum = 0
    for divisor in range(1, limit):
        if number % divisor == 0:
            sum += divisor

    return sum == number
