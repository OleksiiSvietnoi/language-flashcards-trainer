def choose_language():
    print("Choose a language to practice:")
    print("1 — Spanish")
    print("2 — Russian")
    print("3 — Japanese")
    print("4 — French")

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


def main():
    filename = choose_language()
    print(f"You selected: {filename}")


if __name__ == "__main__":
    main()
