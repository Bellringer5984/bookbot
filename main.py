"""
    This module contains functions to read a book from a file, count the number of words and letters in the book, 
    and print a report of these counts. The main function orchestrates these tasks.

    Functions:
        main: Orchestrates the reading of a book, counting words and letters, and printing a report.
        get_book_text: Reads a book from a file and returns the text.
        count_words: Counts the number of words in a given text.
        count_letters: Counts the number of each letter in a given text.
"""
def main():
    """
    Main function to read a book and print a report of word and letter counts.
    """
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(report(text))

def get_book_text(path):
    """
    Reads a book from a given path.

    Args:
        path (str): The path to the book file.

    Returns:
        str: The text of the book.
    """
    with open(path, encoding='utf-8') as f:
        return f.read()

def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split(' ')
    return len(words)

def count_letters(text):
    """
    Counts the number of each letter in a given text.

    Args:
        text (str): The text to count letters in.

    Returns:
        dict: A dictionary with each letter as a key and its count as the value.
    """
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
    """
    Generates a report of the word count and letter counts in a given text.

    Args:
        text (str): The text to generate a report for.

    Returns:
        None
    """
    words = count_words(text)
    letters = count_letters(text)
    letters = list(letters.items())
    letters.sort()
    print("--- Begin Report ---")
    print("Word count:", words)
    for letter in letters:
        print(f"'{letter[0]}' character was found {letter[1]} times.")

main()
