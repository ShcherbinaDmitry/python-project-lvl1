import random


OPERANDS = ('+', '-', '*')


def calc():
    number1 = random.randrange(0, 20)
    number2 = random.randrange(0, 20)
    op = random.randrange(0, 3)
    operand = OPERANDS[op]

    print(f"Question: {number1} {operand} {number2}")

    if (operand == '+'):
        result = number1 + number2
    elif (operand == '-'):
        result = number1 - number2
    elif (operand == '*'):
        result = number1 * number2

    return str(result)
