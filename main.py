def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

def main():
    print(get_book_text("./books/frankenstein.txt"))
    

main()