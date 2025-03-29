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
    stage_0, stage_1, stage_2, stage_3, stage_4,
    stage_5, stage_6, stage_7, stage_8
]

words = [
    "car", "computer", "program", "python",
    "hangman", "game", "work", "house", "cat", "dog"
]


def secret_word(words_lst):
    return random.choice(words_lst)


def main_logic():
    word = secret_word(words)
    guessed = set()
    wrong_guessed = 0
    max_tries = len(stages) - 1
    show_word = ["_" for _ in word]

    print("\nWelcome to Hangman!\n")

    while wrong_guessed <= max_tries:
        stages[wrong_guessed]()
        print(f"\nWord: {' '.join(show_word)}")
        print(f"Guessed letters: {' '.join(sorted(guessed))}")

        user_letter = input("Enter a letter: ").lower().strip()

        if not user_letter or len(user_letter) != 1 or not user_letter.isalpha():
            print("Please enter a single letter!\n")
            continue

        if user_letter in guessed:
            print("You already guessed that letter!\n")
            continue

        guessed.add(user_letter)

        if user_letter in word:
            for i, letter in enumerate(word):
                if letter == user_letter:
                    show_word[i] = user_letter
            if "_" not in show_word:
                stages[wrong_guessed]()
                print("\nYou win!")
                print(f"The word was: {' '.join(show_word)}")
                print("Congratulations, you guessed the word!\n")
                break
        else:
            wrong_guessed += 1
            if wrong_guessed > max_tries:
                print("\nGame over!")
                stages[-1]()
                print(f"You lost! The word was: {word}\n")
                break


main_logic()
