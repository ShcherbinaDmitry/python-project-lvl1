from brain_games.scripts.base import play
from brain_games.scripts.games.progression import progression


def main():
    description = 'What number is missing in the progression?'
    play(description, progression)
