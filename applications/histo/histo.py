# Your code here

def hist(txtfile):
    dct = {}
    with open(txtfile) as f:
        words = f.read()
    for word in words.split():
        word = word.lower()
        if word not in dct:
            dct[word] = '#'
        else:
            dct[word] += '#'
    dct = sorted(sorted(dct.items(), key=lambda x: x[0]))
    dct = dict(dct)
    sorted_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    for pair in sorted_dct:
        print(pair[0], "  ", pair[1])


hist('robin.txt')
