import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_chances(remaining, total):
    plt.figure(figsize=(6, 4))
    plt.bar(['Chances Left'], [remaining], color='red')
    plt.ylim(0, total)
    plt.xlabel("Attempts")
    plt.ylabel("Remaining Chances")
    plt.title("Hangman Game Progress")
    plt.show()

def load_words():
    try:
        df = pd.read_csv("words.txt", header=None, names=['words'])
        words = df['words'].dropna().tolist()
        return words
    except FileNotFoundError:
        print("Error: words.txt file not found. Using default word list.")
        return ['python', 'pandas', 'matplotlib', 'numpy', 'seaborn', 'scipy', 'sklearn']

def play_hangman():
    words = load_words()
    word_to_guess = np.random.choice(words).upper()
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 7
    display_word = ['_'] * len(word_to_guess)
    
    print("Welcome to Hangman! Guess the word.")
    while wrong_guesses < max_attempts and '_' in display_word:
        print("\nCurrent word: ", ' '.join(display_word))
        plot_chances(max_attempts - wrong_guesses, max_attempts)
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    display_word[idx] = guess
        else:
            wrong_guesses += 1
            print(f"Incorrect! {max_attempts - wrong_guesses} attempts left.")
    
    plot_chances(max_attempts - wrong_guesses, max_attempts)
    if '_' not in display_word:
        print("Congratulations! You guessed the word:", word_to_guess)
    else:
        print("You lost! The word was:", word_to_guess)

if __name__ == "__main__":
    play_hangman()
