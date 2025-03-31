def get_book_text(path_to_file):
    from stats import get_num_words
    with open(path_to_file) as f:
        file_contents = f.read()
    get_num_words(file_contents)


def main():
    path_to_file = "books/frankenstein.txt"
    get_book_text(path_to_file)


main()