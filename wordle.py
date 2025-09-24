import random
import sys
import time
from typing import List, Tuple
from pathlib import Path

def printCorrect(s): print("\033[92m["+s+"]\033[00m")
def printClose(s): print("\033[93m["+s+"]\033[00m")
def printWrong(s): print("\033[00m["+s+"]\033[00m")

print("Welcome to TERMINORDLE, also known as Terminal Wordle!")
time.sleep(1)
print("Your goal: guess the 5-letter word.")
time.sleep(1.5)
print("You have 6 attempts.")
time.sleep(1)
print("After each guess, you'll receive feedback:")
time.sleep(1)
print(" - \033[92mGREEN\033[00m: Correct letter in the correct position")
time.sleep(.5)
print(" - \033[93mYELLOW\033[00m: Correct letter in the wrong position")
time.sleep(.5)
print(" - WHITE: Letter not in the word")
time.sleep(1)
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
