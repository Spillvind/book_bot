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

def report_all_characters(book_text):
    report_characters = []
    characters = count_all_characters(book_text)
    for char, count in characters.items():
        one_dict = {"char": char, "num": count}
        report_characters.append(one_dict)
    sorted_report_characters = sorted(report_characters, key=lambda dict: dict["num"], reverse=True)
    return sorted_report_characters