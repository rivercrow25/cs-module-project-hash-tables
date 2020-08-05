import re


def word_count(s):
    # Your code here
    my_dict = {}
    tr = str.maketrans('', '', '":;,.-+=/\\|[]{}()*^&')
    s = s.translate(tr).lower()
    return s

    if len(s) > 1:
        s = re.sub('[\t\r\n".,]', ' ', s)
        s = s.translate({ord(i): None for i in '":,.-+=/\|[]}{()*^&'})

    mylst = s.split(" ")
    if s == '':
        return {}

    for word in mylst:
        if word != "":
            if my_dict.get(word.lower()):
                my_dict[word.lower()] += 1
            else:
                my_dict[word.lower()] = 1
    return my_dict


if __name__ == "__main__":
    print(word_count("a a\ra\na\ta \t\r\n"))
    print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
