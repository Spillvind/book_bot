from stats import count_words
from stats import count_characters

def get_book_text(filepath):
     with open (filepath) as f:
        file_contents = f.read()
     return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    
main()
    




