import random


def hangman():
    # List of words
    words = ["python", "java", "hangman", "developer", "algorithm"]
    word = random.choice(words)

    # Initialize game variables
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in guessed_word:
        print("\nWord: ", " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts -= 1

    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)


# Start the game
if __name__ == "__main__":
    hangman()
