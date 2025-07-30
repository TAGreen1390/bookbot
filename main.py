def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

from stats import word_count
from stats import character_count
from stats import character_sort

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print(f"analysing book found at /books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for char in character_sort(character_count(book_text)):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()