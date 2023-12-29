def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(report(text))
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split(' ')
    return len(words)

def count_letters(text):
    text = text.lower()
    letters = [letter for letter in text if letter.isalpha()]
    letter_dict = {}

    for letter in letters:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def report(text):
    words = count_words(text)
    letters = count_letters(text)
    letters = list(letters.items())
    letters.sort()
    print("--- Begin Report ---")
    print("Word count:", words)
    for letter in letters:
        print(f"'{letter[0]}' character was found {letter[1]} times.")

main()
