from brain_games.scripts.base import play
from brain_games.scripts.games.prime import prime


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play(description, prime)
