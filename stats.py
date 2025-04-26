def count_words(book_text):
    strings = book_text.split()
    num_words = len(strings)
    return num_words

def count_all_characters(book_text):
    strings_lower_case = book_text.lower()
    characters = {}
    for character in strings_lower_case:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters





    

