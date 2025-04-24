def count_words(book_text):
    strings = book_text.split()
    num_words = len(strings)
    return num_words

def count_characters(book_text):
    strings_lower_case = book_text.lower()
    
