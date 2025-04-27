import sys
from stats import count_words
from stats import count_all_characters
from stats import report_all_characters
if len (sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
     with open (filepath) as f:
        file_contents = f.read()
     return file_contents


def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_characters = count_all_characters(book_text)
    report_characters = report_all_characters(book_text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #print(num_characters)
    print("--------- Character Count -------")
    for char_dict in report_characters:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
if __name__ == "__main__":  
    main()