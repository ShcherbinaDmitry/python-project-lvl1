import random


def even():
    number = random.randrange(0, 20)
    print(f"Question: {number}")
    is_even = number % 2 == 0 and 'yes' or 'no'

    return is_even
