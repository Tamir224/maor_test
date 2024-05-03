import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print(display_word(word, guessed_letters))
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! You've run out of attempts.")
                print(f"The word was: {word}")
                break

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word correctly.")
            break

hangman()