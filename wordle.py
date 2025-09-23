import random
import sys
from typing import List, Tuple
from pathlib import Path

print("Welcome to Wordle!")
print("Guess the 5-letter word.")
print("You have 6 attempts.")
print("After each guess, you'll receive feedback:")
print(" - 🟩: Correct letter in the correct position")
print(" - 🟨: Correct letter in the wrong position")
print(" - ⬜: Letter not in the word")
print("Let's begin!")

def main():
    # Allow passing a custom wordlist path as CLI arg
    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = WORDLIST_PATH

    words = load_wordlist(path)
    if not words:
        print("No 5-letter words available. Please provide a wordlist.")
        sys.exit(1)

    target = pick_target(words)
    max_guesses = 6

    print("Welcome to Terminal Wordle! Guess the 5-letter word in 6 tries.")
    print("Green = correct place, Yellow = wrong place, Gray = not in word.")
    # Uncomment to debug/cheat:
    # print(f"(DEBUG) Target is: {target}")

    guesses = 0
    while guesses < max_guesses:
        guesses += 1
        while True:
            guess = input(f"\nGuess {guesses}/{max_guesses}: ").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Please enter a 5-letter word using letters only.")
                continue
            if guess not in words:
                print("Word not in dictionary. Try again.")
                continue
            break

        fb = get_feedback(guess, target)
        print(colored_output(fb))

        if all(color == "green" for (_l, color) in fb):
            print(f"\nYou got it in {guesses} guess{'es' if guesses != 1 else ''}! 🎉")
            return

    print(f"\nOut of guesses — the word was: {target.upper()}. Better luck next time!")
