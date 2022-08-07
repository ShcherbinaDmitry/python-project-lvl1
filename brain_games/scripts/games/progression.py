from random import randrange


def progression():
    length = randrange(5, 11)
    position = randrange(0, length)
    start = randrange(0, 100)
    step = randrange(1, 11)

    current = start

    question = 'Question:'

    for i in range(0, length):
        if (i == position):
            question += ' ..'
            answer = current
        else:
            question += f' {current}'

        current += step

    print(question)

    return str(answer)