# Open the book's source location, read the contents and assign it to a string variable
def get_book_text(file_source):
    with open(file_source) as f:
        book_string = f.read()
    return book_string


def main():
    from stats import get_num_words
    from stats import get_character_count
    
    path_to_file = "books/frankenstein.txt"
    book_string = get_book_text(path_to_file)
    wordcount = get_num_words(book_string)
    character_count = get_character_count(book_string)

    # PRINT REPORT
    print("")
    print("============ BOOKBOT ============")
    print("")
    print(f"Analyzing book found at {path_to_file}...")
    print("")
    print("----------- Word Count ----------")
    print("")
    print(f"Found {wordcount} total words")
    print("")
    print("--------- Character Count -------")
    print("")
    for key, value in character_count.items():
        print(f"{key}: {value}")


main()