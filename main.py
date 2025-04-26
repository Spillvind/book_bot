from stats import count_words
from stats import count_all_characters

def get_book_text(filepath):
     with open (filepath) as f:
        file_contents = f.read()
     return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_characters = count_all_characters(book_text)
    print(f"{num_words} words found in the document")
    print(num_characters)
    
main()
    




