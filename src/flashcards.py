import os
import random
from colorama import Fore, Style, init
init(autoreset=True)


def choose_language():
    print(Fore.CYAN + "Choose a language to practice:")
    print("1 - Spanish")
    print("2 - Russian")
    print("3 - Japanese")
    print("4 - French")

    choice = input("Enter number: ").strip()

    if choice == "1":
        return "spanish.txt"
    elif choice == "2":
        return "russian.txt"
    elif choice == "3":
        return "japanese.txt"
    elif choice == "4":
        return "french.txt"
    else:
        print(Fore.YELLOW + "Invalid choice. Try again.")
        return choose_language()


def choose_mode():
    while True:
        print("\nChoose mode:")
        print("1 - Normal (word -> translation)")
        print("2 - Reverse (translation -> word)")
        mode = input("Enter mode (1/2): ").strip()

        if mode == "1":
            return False
        elif mode == "2":
            return True
        else:
            print("Invalid choice. Please enter 1 or 2.")


def choose_rounds(default=5):
    print(Fore.CYAN + f"\nHow many questions? (default {default})")
    val = input("Enter number or press Enter: ").strip()
    if val == "":
        return default
    try:
        n = int(val)
        if n > 0:
            return n
        else:
            print(Fore.YELLOW + "Number must be positive. Using default.")
            return default
    except ValueError:
        print(Fore.YELLOW + "Invalid number. Using default.")
        return default


def load_words(filename):
    script_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(script_dir)
    path = os.path.join(project_root, "data", filename)

    lines = []
    try:
        f = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        print(Fore.RED + "File not found:", path)
        return lines

    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
    f.close()
    return lines


def simple_quiz(lines, rounds=5, reverse=False):
    if not lines:
        print(Fore.RED + "No words to quiz.")
        return

    pool = lines.copy()
    score = 0
    wrong_answers = []

    for i in range(rounds):
        if not pool:
            print(Fore.YELLOW + "No more unique questions left.")
            break

        pair = random.choice(pool)
        pool.remove(pair)

        parts = pair.split("|")

        if len(parts) == 3:
            word = parts[0].strip()
            reading = parts[1].strip()
            translation = parts[2].strip()
        elif len(parts) == 2:
            word = parts[0].strip()
            reading = ""
            translation = parts[1].strip()
        else:
            word = pair.strip()
            reading = ""
            translation = ""

        if reverse:
            question = translation or word
            answer = word
        else:
            question = word + (f" ({reading})" if reading else "")
            answer = translation

        print(Fore.CYAN + f"\nQuestion {i+1}/{rounds}: Translate -> {question}")
        user = input("Your answer (or q to quit): ").strip()

        if user.lower() == "q":
            print(Fore.YELLOW + "Quiz stopped by user.")
            break

        if answer and user.lower() == answer.lower():
            print(Fore.GREEN + "Correct!\n")
            score += 1
        else:
            print(Fore.RED + "Wrong. Correct: " + (answer if answer else "(no answer available)") + "\n")
            wrong_answers.append((question, answer))

    asked = i + 1 if user.lower() != "q" else i
    print(Fore.CYAN + f"Quiz finished. Score: {score} / {asked}")

    if wrong_answers:
        print(Fore.YELLOW + "\nWords you should review:")
        for q, a in wrong_answers:
            print(f"- {q} -> {a}")

    return {
        "asked": asked,
        "correct": score,
        "wrong": wrong_answers
    }
