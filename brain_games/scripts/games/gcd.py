import random
import math

def gcd():
    number1 = random.randrange(0, 100)
    number2 = random.randrange(0, 100)

    print(f'Question: {number1} {number2}')

    max = number1 > number2 and number1 or number2
    min = number1 < number2 and number1 or number2

    if (max % min == 0):
        return str(min)

    for i in range(math.floor(min / 2) + 1, 0, -1):
        if (number1 % i == 0 and number2 % i == 0):
            return str(i)

    return 'Error finding gcd'