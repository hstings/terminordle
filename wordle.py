import random

def wordleFeedbackSquares(guess, target):
    green = "\033[42m"
    yellow = "\033[43m"
    gray = "\033[100m"
    reset = "\033[0m"

    result = [""] * len(guess)
    targetLetters = list(target)

    # First pass: greens
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = f"{green} {ch.upper()} {reset}"
            targetLetters[i] = None  # consume

    # Second pass: yellows
    for i, ch in enumerate(guess):
        if result[i] == "" and ch in targetLetters:
            result[i] = f"{yellow} {ch.upper()} {reset}"
            targetLetters[targetLetters.index(ch)] = None
        elif result[i] == "":
            result[i] = f"{gray} {ch.upper()} {reset}"

    return " ".join(result)


def emptyRow(wordLength):
    gray = "\033[100m"
    reset = "\033[0m"
    return " ".join([f"{gray}   {reset}"] * wordLength)


def playWordle(wordList, solutionList):
    targetWord = random.choice(solutionList)
    guesses = []
    attempt = 0

    for attempt in range(1, 6):
        guess = input(f"\nAttempt {attempt}/{6}: ").strip().lower()

        # Validate guess
        if len(guess) != 5:
            print(f"Please enter a {5}-letter word.")
            continue
        elif guess not in wordList:
            print("Not in word list.")
            continue

        feedback = wordleFeedbackSquares(guess, targetWord)
        guesses.append(feedback)

        # Print full board
        print("\nYour board:")
        for g in guesses:
            print(g)
            attempt += 1
        for _ in range(6 - len(guesses)):
            print(emptyRow(5))

        if guess == targetWord:
            messages = ["Genius", "Magnificent", "Impressive", "Splendid", "Great", "Phew"]
            print(messages[attempt - 1])
            return

    print(f"\n❌ Out of attempts! The word was '{targetWord.upper()}'.")

with open("resources/words.txt", "r") as f:
    wordList = [w.strip().lower() for w in f if w.strip()]

with open("resources/wordSolutions.txt", "r") as f:
    solutionList = [w.strip().lower() for w in f if w.strip()]

print("Welcome to TERMINORDLE, also known as Terminal Wordle! Guess the 5-letter word.")
playWordle(wordList, solutionList)
