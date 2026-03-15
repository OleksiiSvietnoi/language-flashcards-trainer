from flashcards import choose_language, load_words, simple_quiz

def main():
    filename = choose_language()
    lines = load_words(filename)
    simple_quiz(lines)

if __name__ == "__main__":
    main()