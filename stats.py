def get_num_words(file_contents):
    words = file_contents.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    print(wordcount, "words found in the document")