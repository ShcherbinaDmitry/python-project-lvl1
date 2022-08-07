from brain_games.scripts.base import play
from brain_games.scripts.games.even import even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    play(description, even)
