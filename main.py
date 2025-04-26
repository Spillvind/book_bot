from stats import count_words
from stats import count_all_characters
from stats import report_all_characters

def get_book_text(filepath):
     with open (filepath) as f:
        file_contents = f.read()
     return file_contents


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_characters = count_all_characters(book_text)
    report_characters = report_all_characters(book_text)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(num_characters)
    print("--------- Character Count -------")
    for char_dict in report_characters:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

    
main()
    




