'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case: word is ""
    if word == "":
        return 0
    
    # recursive case:
    # look at last two letters of word
    last_two_letters = word[-2:]
    # if they equal th (lower case), return 1 + count_th(word[:-2])
    if last_two_letters == "th":
        return 1 + count_th(word[:-2])
    # if they don't, return count_th(word([:-1]))
    else:
        return count_th(word[:-1])

    
