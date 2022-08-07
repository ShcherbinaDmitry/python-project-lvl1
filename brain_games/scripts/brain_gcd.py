from brain_games.scripts.base import play
from brain_games.scripts.games.gcd import gcd


def main():
    description = 'Find the greatest common divisor of given numbers.'
    play(description, gcd)
