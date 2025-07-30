import sys

def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

from stats import word_count
from stats import character_count
from stats import character_sort

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"analysing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for char in character_sort(character_count(book_text)):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()