from stats import *
from sys import argv

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    url = argv[1] #"books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {url}...")
    book_text = get_book_text(url)
    text_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {text_words} total words")
    print("--------- Character Count -------")
    characters = count_characters(book_text)
    sorted_characters = sort_dict(characters)
    for char in sorted_characters:
        if char.isalpha():
            print(f"{char}: {sorted_characters[char]}")
    print("============= END ===============")

main()

