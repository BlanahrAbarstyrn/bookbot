# Open the book's source location, read the contents and assign it to a string variable
def get_book_text(file_source):
    with open(file_source) as f:
        book_string = f.read()
    return book_string


def main():
    from stats import get_num_words
    from stats import get_character_count

    import sys

    # Check if the correct number of arguments were provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]

    #path_to_file = "books/frankenstein.txt"
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
    # END REPORT

main()