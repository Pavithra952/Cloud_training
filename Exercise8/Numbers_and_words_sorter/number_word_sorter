import sys


def input_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number (0 to stop): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers


def input_words():
    words = []
    while True:
        word = input("Enter a word (END to stop): ")
        if word == "END":
            break
        words.append(word)
    return words


if __name__ == "__main__":
    print("Enter numbers:")
    numbers = input_numbers()

    print("\nAscending Order:")
    numbers.sort()
    for num in numbers:
        print(num, end=' ')

    print("\nDescending Order:")
    numbers.sort(reverse=True)
    for num in numbers:
        print(num, end=' ')

    print("\nEnter words:")
    words = input_words()

    print("\nAscending Order:")
    words.sort()
    for word in words:
        print(word, end=' ')

    print("\nDescending Order:")
    words.sort(reverse=True)
    for word in words:
        print(word, end=' ')

