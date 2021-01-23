def print_upper_words(words, must_start_with):
    """Accepts a list of strings and a list of letters. If a string starts
    with one of the letters in the list, it will be printed in all caps"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())