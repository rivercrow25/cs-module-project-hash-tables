def no_dups(s):
    # Your code here
    dct = {}
    sentance = ""
    for word in s.split(" "):
        if dct.get(word):
            dct[word] += 1
        else:
            dct[word] = 1
    for word in dct.items():
        sentance += word[0] + " "
    sentance = sentance.strip()
    return sentance


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
