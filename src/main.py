import os
import random

def choose_language():
    print("Choose a language to practice:")
    print("1 - Spanish")
    print("2 - Russian")
    print("3 - Japanese")
    print("4 - French")

    choice = input("Enter number: ")

    if choice == "1":
        return "spanish.txt"
    elif choice == "2":
        return "russian.txt"
    elif choice == "3":
        return "japanese.txt"
    elif choice == "4":
        return "french.txt"
    else:
        print("Invalid choice. Try again.")
        return choose_language()


def load_words(filename):

    script_dir = os.path.dirname(__file__)

    project_root = os.path.dirname(script_dir)

    path = os.path.join(project_root, "data", filename)

    lines = []
    try:
        f = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found:", path)
        return lines

    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
    f.close()
    return lines



def simple_quiz(lines, rounds=5):
    if not lines:
        print("No words to quiz.")
        return

    pool = lines.copy()

    score = 0
    for i in range(rounds):
        if not pool:
            print("No more questions left.")
            break

        pair = random.choice(pool)
        pool.remove(pair)

        parts = pair.split("|")

        if len(parts) == 3:
            question = parts[0].strip() + " (" + parts[1].strip() + ")"
            answer = parts[2].strip()
        elif len(parts) == 2:
            question = parts[0].strip()
            answer = parts[1].strip()
        else:
            question = pair
            answer = ""

        print(f"Question {i+1}/{rounds}: Translate -> {question}")
        user = input("Your answer (or q to quit): ").strip()

        if user.lower() == "q":
            break

        if user.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print("Wrong. Correct:", answer, "\n")

    print("Quiz finished. Score:", score, "/", i+1)


def main():
    filename = choose_language()
    lines = load_words(filename)
    simple_quiz(lines)


if __name__ == "__main__":
    main()