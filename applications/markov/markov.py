import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()


dct = {}
lst = words.split(' ')
# TODO: analyze which words can follow other words
# Your code here
for i in range(len(lst) - 1):
    word = lst[i]
    nxt_word = lst[i+1]

    if word not in dct:
        dct[word] = [nxt_word]
    else:
        dct[word].append(nxt_word)


start_words = []
for key in dct.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)
# TODO: construct 5 random sentences
# Your code here
word = random.choice(start_words)
stopped = False
punctuations = "?!."


def paragraph():
    global word
    global stopped
    count = 0
    line5 = False
    while not line5:
        while not stopped:
            print(word, end=" ")
            if word[-1] in punctuations or len(word) > 1 and word[-2] in punctuations:
                stopped = True
            following = dct[word]
            word = random.choice(following)
        if count >= 6:
            line5 = True
        count += 1


paragraph()
