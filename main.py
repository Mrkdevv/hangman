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
    word = secret_word(words)
    guessed = set()
    wrong_guessed = 0
    max_tries = len(stages) - 1
    show_word = ["_" for _ in word]

    print("Hangman Game!\n")
    while wrong_guessed <= max_tries:

        stages[wrong_guessed]()
        print("Secret word is:" ," ".join(show_word))
        print("Guessed letters" ," ".join(sorted(guessed)))

        user_letter = str(input("Enter a letter")).lower()

        if not user_letter or len(user_letter) != 1:
            print("Enter one letter!")
            continue

        if user_letter in guessed:
            print("You already write this letter!")
            continue

        guessed.add(user_letter)

        if user_letter in word:

