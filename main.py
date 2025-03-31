def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
    num_words(file_contents)


def num_words(file_contents):
    words = file_contents.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    print(wordcount, "words found in the document")


def main():
    path_to_file = "books/frankenstein.txt"
    get_book_text(path_to_file)


main()