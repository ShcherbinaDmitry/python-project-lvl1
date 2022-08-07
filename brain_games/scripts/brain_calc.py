from brain_games.scripts.base import play
from brain_games.scripts.games.calc import calc


def main():
    description = 'Whta is the result of the expression?'
    play(description, calc)
