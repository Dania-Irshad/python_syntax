def print_upper_words(words, must_start_with):
    """Print words in a list to all upper case letter words 
    
    For example:

        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

   should print:

        "HELLO", "HEY", "YO", and "YES"
    """

    for word in words:
        for letter in must_start_with:
            if letter == word[0]:
                upper_word = word.upper()
                print(upper_word)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})