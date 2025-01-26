import random

def hangman():
    word_list = ['python', 'javascript', 'hangman', 'developer', 'programming', 'code']
    word = random.choice(word_list).lower()
    guessed_word = ['_'] * len(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print(" ".join(guessed_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print(" ".join(guessed_word))

        if '_' not in guessed_word:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
