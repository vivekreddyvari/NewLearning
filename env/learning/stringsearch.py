word1 = input('Enter your word: ').lower()
word2 = input('Enter your string: ').lower()


def find_word(word1, word2):
    """
    The function will search for word in the string
    word1: (str) user input
    word2: (str) user input a mixed alphabets
    """
    # splitter
    def split(word):
        return [char for char in word]

    # split the word1 and word2 into list alphabets
    word1_split = split(word1)
    word2_split = split(word2)

    # search each alphabet of word1 present in word2
    x = []
    for char in word1_split:
        x.append(str(word2.find(char)))
    # calculate the result by multiplying
    result = 1
    for n in x:
        if int(n) > 0:
            result = result * int(n)
        elif int(n) < 0:
            result = result * int(n)

    if result > 0:
        return 'Yes'
    else:
        return 'No'




print(find_word(word1, word2))