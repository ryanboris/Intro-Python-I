# implement longestString function (done originally in JS) in python


def longest_word(str):
    word_list = str.split(" ")
    longest_word = 0
    word = ''
    for item in word_list:
        if len(item) > longest_word:
            longest_word = len(item)
            word = item
    return word


print(longest_word("This is a string"))
