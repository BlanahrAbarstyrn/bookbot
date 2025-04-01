# Receive in a book in string format, split the string into individual words, and then count how many words are in the list
def get_num_words(book_string):
    words = book_string.split()
    for wordcount in range(0, len(words)):
        wordcount += 1
    return wordcount


# Receive in a book in string format, change the text to all lower case, create a dictionary for each character and its qty within the book
def get_character_count(book_string):
    # Create an empty dictionary to store the count of each character
    count_of_char = {}
    # Change all letters to lowercase
    no_big_letters = book_string.lower()
    # Loop through each character in the string
    for character in no_big_letters:
        # If the character is already in the dictionary, increment its count
        if character in count_of_char:
            count_of_char[character] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            count_of_char[character] = 1
    return count_of_char