import random
import math


def prime():
    number = random.randrange(1, 51)

    print(f'Question: {number}')

    for i in range(2, math.floor(number / 2) + 1):
        if (number % i == 0):
            return 'no'

    return 'yes'
