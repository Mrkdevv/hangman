import random


def stage_0():
    print("""






    =========
    """)


def stage_1():
    print("""
      |
      |
      |
      |
      |
    =========
    """)


def stage_2():
    print("""
  +---+
      |
      |
      |
      |
      |
    =========
    """)


def stage_3():
    print("""
  +---+
  |   |
  O   |
      |
      |
      |
    =========
    """)


def stage_4():
    print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
    =========
    """)


def stage_5():
    print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
    =========
    """)


def stage_6():
    print("""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
    =========
    """)


def stage_7():
    print("""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
    =========
    """)


def stage_8():
    print("""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
    =========
    """)


stages = [
    stage_0,
    stage_1,
    stage_2,
    stage_3,
    stage_4,
    stage_5,
    stage_6,
    stage_7,
    stage_8
]


words = [
    "car",
    "computer",
    "program",
    "python",
    "hangman",
    "game",
    "work",
    "house",
    "cat",
    "dog"
]


def secret_word(words_lst):
    return random.choice(words_lst)

def main_logic():
    guessed = set()
    wrong_guessed = 0
    max_tries = len(stages)
    while wrong_guessed < max_tries:
        print("Hangman Game!")
        stages[wrong_guessed]()
        print("Secret word is:" "".join("s"))
