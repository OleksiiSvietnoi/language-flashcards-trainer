from flashcards import choose_language, load_words, choose_mode, choose_rounds, simple_quiz

def main():
    filename = choose_language()
    lines = load_words(filename)
    if not lines:
        return

    reverse = choose_mode()
    rounds = choose_rounds(default=5)
    simple_quiz(lines, rounds=rounds, reverse=reverse)

if __name__ == "__main__":
    main()

