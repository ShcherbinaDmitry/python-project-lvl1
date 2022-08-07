import prompt


def play(description, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print(description)

    wins = 0
    endgame_message = f'Congratulations, {name}!'

    while (wins < 3):
        correct_answer = game()

        user_answer = prompt.string('Your answer: ')

        if (user_answer == correct_answer):
            print('Correct!')
            wins += 1
        else:
            print(f"'{user_answer}' was wrong answer ;(. Correct answer was '{correct_answer}'")
            endgame_message = f'Let\'s try again, {name}!'
            break

    print(endgame_message)
