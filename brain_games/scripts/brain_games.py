#!/usr/bin/env python3
from brain_games.cli import welcome_user


def initial_welcome():
    print('Welcome to the Brain Games!')


def main():
    initial_welcome()

    welcome_user()


if __name__ == '__main__':
    main()
