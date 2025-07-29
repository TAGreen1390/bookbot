def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

from stats import word_count
from stats import character_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(f"{word_count(book_text)} words found in the document")
    print(character_count(book_text))

main()